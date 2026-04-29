document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.querySelector("[data-chat-toggle]");
    const closeButton = document.querySelector("[data-chat-close]");
    const widget = document.querySelector("[data-chat-widget]");
    const form = document.querySelector("[data-chat-form]");
    const managerForm = document.querySelector("[data-form-type='consultation-send']");

    if (toggleButton && widget) {
        toggleButton.addEventListener("click", function () {
            widget.classList.toggle("hidden");
        });

        if (closeButton) {
            closeButton.addEventListener("click", function () {
                widget.classList.add("hidden");
            });
        }
    }

    // WebSocket connection
    const chatSocket = new WebSocket(
        'ws://' + window.location.host + '/ws/chat/' + roomId + '/'
    );

    chatSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        const thread = document.querySelector(".chat-thread");
        if (thread) {
            // For manager
            const row = document.createElement("div");
            row.className = "chat-row " + (data.user_id == userId ? "right" : "left");
            if (data.user_id == userId) {
                row.innerHTML = `
                    <div class="chat-time">${new Date(data.timestamp).toLocaleTimeString()}</div>
                    <div class="chat-bubble solid">${data.message}</div>
                    <div class="manager-avatar mini"></div>
                `;
            } else {
                row.innerHTML = `
                    <div class="conversation-avatar tiny avatar-neutral"></div>
                    <div class="chat-bubble outline">${data.message}</div>
                `;
            }
            thread.appendChild(row);
            thread.scrollTop = thread.scrollHeight;
        } else if (widget) {
            // For customer
            const body = widget.querySelector(".chat-body");
            const row = document.createElement("div");
            row.className = "chat-row " + (data.user_id == userId ? "right" : "left");
            row.innerHTML =
                '<p class="chat-bubble"></p>' +
                '<span class="chat-stamp">' + new Date(data.timestamp).toLocaleTimeString() + '</span>';
            row.querySelector(".chat-bubble").textContent = data.message;
            body.appendChild(row);
            body.scrollTop = body.scrollHeight;
        }
    };

    chatSocket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly');
    };

    if (form) {
        form.addEventListener("submit", function (event) {
            event.preventDefault();
            const input = form.querySelector("input[name='message']");
            if (!input || !input.value.trim()) {
                return;
            }

            const message = input.value.trim();

            // Add message to UI immediately
            const body = widget.querySelector(".chat-body");
            const row = document.createElement("div");
            row.className = "chat-row right";
            row.innerHTML =
                '<p class="chat-bubble"></p>' +
                '<span class="chat-stamp">' + new Date().toLocaleTimeString() + '</span>';
            row.querySelector(".chat-bubble").textContent = message;
            body.appendChild(row);
            body.scrollTop = body.scrollHeight;

            chatSocket.send(JSON.stringify({
                'message': message,
                'user_id': userId
            }));

            input.value = "";
        });
    }

    if (managerForm) {
        managerForm.addEventListener("submit", function (event) {
            event.preventDefault();
            const input = managerForm.querySelector("input[name='message']");
            const warning = document.querySelector("[data-chat-empty-warning]");
            if (!input || !input.value.trim()) {
                if (warning) warning.classList.remove("hidden");
                return;
            }
            if (warning) warning.classList.add("hidden");

            const message = input.value.trim();

            // Add to chat-thread
            const thread = document.querySelector(".chat-thread");
            const row = document.createElement("div");
            row.className = "chat-row right";
            row.innerHTML = `
                <div class="chat-time">${new Date().toLocaleTimeString()}</div>
                <div class="chat-bubble solid">${message}</div>
                <div class="manager-avatar mini"></div>
            `;
            thread.appendChild(row);
            thread.scrollTop = thread.scrollHeight;

            chatSocket.send(JSON.stringify({
                'message': message,
                'user_id': userId
            }));

            input.value = "";
        });
    }
});
