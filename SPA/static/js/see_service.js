const searchInput = document.getElementById("search");
const priceSort = document.getElementById("priceSort");
const filterButtons = document.querySelectorAll(".filter-chip");
const serviceList = document.getElementById("serviceList");
const emptyState = document.getElementById("emptyState");

if (searchInput && priceSort && serviceList && emptyState) {
    const cards = Array.from(serviceList.querySelectorAll(".card"));
    let activeCategory = "all";

    const applyFilters = () => {
        const keyword = searchInput.value.trim().toLowerCase();
        const sortMode = priceSort.value;

        const visibleCards = cards.filter((card) => {
            const category = card.dataset.category;
            const name = (card.dataset.name || "").toLowerCase();
            const matchesCategory = activeCategory === "all" || category === activeCategory;
            const matchesKeyword = !keyword || name.includes(keyword);
            const visible = matchesCategory && matchesKeyword;

            card.classList.toggle("hidden", !visible);
            return visible;
        });

        const sortedCards = [...visibleCards].sort((a, b) => {
            const priceA = Number(a.dataset.price || 0);
            const priceB = Number(b.dataset.price || 0);

            if (sortMode === "asc") {
                return priceA - priceB;
            }

            if (sortMode === "desc") {
                return priceB - priceA;
            }

            return cards.indexOf(a) - cards.indexOf(b);
        });

        sortedCards.forEach((card) => serviceList.appendChild(card));
        emptyState.classList.toggle("hidden", visibleCards.length > 0);
    };

    filterButtons.forEach((button) => {
        button.addEventListener("click", () => {
            activeCategory = button.dataset.category;
            filterButtons.forEach((item) => item.classList.remove("active"));
            button.classList.add("active");
            applyFilters();
        });
    });

    searchInput.addEventListener("input", applyFilters);
    priceSort.addEventListener("change", applyFilters);
    applyFilters();
}
