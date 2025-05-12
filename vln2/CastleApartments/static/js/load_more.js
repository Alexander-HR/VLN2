document.addEventListener("DOMContentLoaded", function() {
    const loadMoreBtn = document.getElementById("load-more");

    if (loadMoreBtn) {
        loadMoreBtn.addEventListener("click", function() {
            const nextPage = this.dataset.next;

            fetch(`/?page=${nextPage}`, {
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            })
            .then(response => response.json())
            .then(data => {
                const grid = document.getElementById("property-grid");
                grid.insertAdjacentHTML("beforeend", data.html);

                if (data.has_next) {
                    this.dataset.next = data.next_page;
                } else {
                    document.getElementById("load-more-container").remove();
                }
            });
        });
    }
});
