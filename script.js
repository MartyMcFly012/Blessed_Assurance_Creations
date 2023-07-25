var products = [
    { name: "Product 1", description: "Description 1", image: "product1.jpg" },
    { name: "Product 2", description: "Description 2", image: "product2.jpg" },
    // Add more products here
];

function search() {
    var searchInput = document.getElementById("search-input").value;
    var filteredProducts = products.filter(function (product) {
        // Match the search input against the product name or description
        return product.name.toLowerCase().includes(searchInput.toLowerCase()) ||
            product.description.toLowerCase().includes(searchInput.toLowerCase());
    });

    var searchResultsContainer = document.getElementById("search-results");
    searchResultsContainer.innerHTML = ""; // Clear previous results

    if (filteredProducts.length > 0) {
        filteredProducts.forEach(function (product) {
            // Create HTML elements for each filtered product
            var productDiv = document.createElement("div");
            productDiv.classList.add("product");

            var image = document.createElement("img");
            image.src = product.image;
            image.alt = product.name;
            image.classList.add("product-image");
            productDiv.appendChild(image);

            var name = document.createElement("h3");
            name.textContent = product.name;
            productDiv.appendChild(name);

            var description = document.createElement("p");
            description.textContent = product.description;
            productDiv.appendChild(description);

            // Append the product div to the search results container
            searchResultsContainer.appendChild(productDiv);
        });
    } else {
        var noResultsMessage = document.createElement("p");
        noResultsMessage.textContent = "No results found.";
        searchResultsContainer.appendChild(noResultsMessage);
    }

    var encodedQuery = encodeURIComponent(searchInput); // Encode the search query

    // Redirect the user to the search results page
    window.location.href = "search-results.html?query=" + encodedQuery;

    const navSlide = () => {
        const burger = document.querySelector('.burger');
        const nav = document.querySelector('.nav-links');
        const dropdownMenu = document.querySelector('.dropdown-menu');
      
        burger.addEventListener('click', () => {
          nav.classList.toggle('nav-active');
          dropdownMenu.classList.toggle('nav-active');
        });
      };
      
      navSlide();
}
