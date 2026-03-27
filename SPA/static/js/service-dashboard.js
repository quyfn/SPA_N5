const body = document.body;
const backdrop = document.querySelector("[data-backdrop]");
const modals = document.querySelectorAll(".modal");

function openModal(modalId) {
    modals.forEach((modal) => modal.classList.add("hidden"));
    const target = document.getElementById(modalId);
    if (!target) {
        return;
    }
    target.classList.remove("hidden");
    backdrop.classList.remove("hidden");
    body.classList.add("modal-open");
}

function closeAllModals() {
    modals.forEach((modal) => modal.classList.add("hidden"));
    backdrop.classList.add("hidden");
    body.classList.remove("modal-open");
}

document.querySelectorAll("[data-modal-target]").forEach((button) => {
    button.addEventListener("click", () => {
        openModal(button.dataset.modalTarget);
    });
});

document.querySelectorAll("[data-close-modal]").forEach((button) => {
    button.addEventListener("click", closeAllModals);
});

backdrop.addEventListener("click", closeAllModals);

function normalizePrice(value) {
    return Number(value.replace(/\./g, "").replace(/\s/g, ""));
}

function validateForm(form) {
    const formType = form.dataset.formType;

    if (formType === "add-service" || formType === "edit-service") {
        const name = form.querySelector('[name="name"]').value.trim();
        const description = form.querySelector('[name="description"]').value.trim();
        const price = normalizePrice(form.querySelector('[name="price"]').value.trim());

        if (!name) {
            return "error-empty-name";
        }
        if (!description) {
            return "error-empty-description";
        }
        if (!Number.isFinite(price) || price <= 0) {
            return "error-invalid-price";
        }
        return "success-save-service";
    }

    if (formType === "update-price") {
        const newPrice = normalizePrice(form.querySelector('[name="new_price"]').value.trim());
        if (!Number.isFinite(newPrice) || newPrice <= 0) {
            return "error-invalid-price";
        }
        return "success-save-service";
    }

    return "success-save-service";
}

document.querySelectorAll("form[data-form-type]").forEach((form) => {
    form.addEventListener("submit", (event) => {
        event.preventDefault();

        if (form.dataset.formType === "reply-feedback") {
            const value = form.querySelector('[name="reply"]').value.trim();
            if (!value) {
                openModal("reply-empty-modal");
                return;
            }
            if (value.toLowerCase().includes("fail")) {
                openModal("reply-failed-modal");
                return;
            }
            openModal("reply-success-modal");
            return;
        }

        openModal(validateForm(form));
    });
});
