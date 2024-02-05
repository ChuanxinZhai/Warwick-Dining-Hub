// data
let allProducts = [
    { name: 'Americano', category: 'Coffee', price: 2.5, size: '200ml', image: 'Americano.png', facility: 'StarBucks Cafe' },
    { name: 'Americano', category: 'Coffee', price: 2.5, size: '200ml', image: 'Americano.png', facility: 'StarBucks Cafe' },
    { name: 'Latte', category: 'Coffee', price: 3.0, size: '300ml', image: 'Latte.png', facility: 'StarBucks Cafe' },
    { name: 'Cappuccino', category: 'Coffee', price: 3.0, size: '200ml', image: 'Cappuccino.png', facility: 'StarBucks Cafe' },
    { name: 'Caramel macchiato', category: 'Coffee', price: 3.0, size: '250ml', image: 'Caramel_macchiato.png', facility: 'StarBucks Cafe' },
    { name: 'Hamburger', category: 'Food', price: 9.0, size: '600g', image: 'Hamburger.png', facility: 'The Beautiful Duck Restaurant' },
    { name: 'Sandwich', category: 'Food', price: 7.5, size: '450g', image: 'Sandwich.png', facility: 'The Beautiful Duck Restaurant' },
    { name: 'Chips', category: 'Food', price: 1.5, size: '100g', image: 'Chips.png', facility: 'The Beautiful Duck Restaurant' },
    { name: 'Ramen', category: 'Food', price: 8.0, size: '800g', image: 'Ramen.png', facility: 'The Beautiful Duck Restaurant' },
    { name: 'Hot dog', category: 'Food', price: 2.5, size: '100g', image: 'Hot_dog.png', facility: 'The Beautiful Duck Restaurant' },
    { name: 'Mojito', category: 'Wine', price: 6.0, size: '400ml', image: 'Mojito.png', facility: 'Terrace Bar' },
    { name: 'Margarita', category: 'Wine', price: 5.0, size: '200ml', image: 'Margarita.png', facility: 'Terrace Bar' },
    { name: 'Tequila sunrise', category: 'Wine', price: 5.5, size: '400ml', image: 'Tequila_sunrise.png', facility: 'Terrace Bar' },
    { name: 'Long island iced tea', category: 'Wine', price: 7.0, size: '450ml', image: 'Long_island_iced_tea.png', facility: 'Terrace Bar' },
    { name: 'Beer', category: 'Wine', price: 3.0, size: '600ml', image: 'Beer.png', facility: 'Terrace Bar' },
    { name: 'Whiskey', category: 'Wine', price: 10.0, size: '500ml', image: 'Whiskey.png', facility: 'Terrace Bar' },
    { name: 'Vodka', category: 'Wine', price: 11.0, size: '500ml', image: 'Vodka.png', facility: 'Terrace Bar' },
    { name: 'Gin', category: 'Wine', price: 11.5, size: '500ml', image: 'Gin.png', facility: 'Terrace Bar' },
    { name: 'Rice', category: 'Food', price: 1.0, size: '300g', image: 'Rice.png', facility: 'The Beautiful Duck Restaurant' },
    { name: 'Steak', category: 'Food', price: 15.0, size: '1000g', image: 'Steak.png', facility: 'The Beautiful Duck Restaurant' },
    { name: 'Barbecue', category: 'Food', price: 20.0, size: '1200g', image: 'Barbecue.png', facility: 'The Beautiful Duck Restaurant' },
    { name: 'Pizza', category: 'Food', price: 7.0, size: '700g', image: 'Pizza.png', facility: 'The Beautiful Duck Restaurant' },
    { name: 'Spaghetti', category: 'Food', price: 8.0, size: '900g', image: 'Spaghetti.png', facility: 'The Beautiful Duck Restaurant' },
    { name: 'Curry', category: 'Food', price: 6.0, size: '800g', image: 'Curry.png', facility: 'The Beautiful Duck Restaurant' },
    { name: 'Espresso', category: 'Coffee', price: 2.8, size: '300ml', image: 'Espresso.png', facility: 'StarBucks Cafe' },
    { name: 'Mocha', category: 'Coffee', price: 3.3, size: '400ml', image: 'Mocha.png', facility: 'StarBucks Cafe' },
    { name: 'Blackcafe', category: 'Coffee', price: 2.3, size: '350ml', image: 'Blackcafe.png', facility: 'StarBucks Cafe' },
    { name: 'Frappuccino', category: 'Coffee', price: 5.0, size: '370ml', image: 'Frappuccino.png', facility: 'StarBucks Cafe' },
    { name: 'Italian coffee', category: 'Coffee', price: 3.0, size: '280ml', image: 'Italian_coffee.png', facility: 'StarBucks Cafe' },
    { name: 'Milk', category: 'Coffee', price: 1.5, size: '250ml', image: 'Milk.png', facility: 'StarBucks Cafe' },
    { name: 'Cider', category: 'Wine', price: 3.5, size: '330ml', image: 'Cider.png', facility: 'Terrace Bar' },
    { name: 'Brandy', category: 'Wine', price: 10.5, size: '300ml', image: 'Brandy.png', facility: 'Terrace Bar' },
    { name: 'Rum', category: 'Wine', price: 12.5, size: '400ml', image: 'Rum.png', facility: 'Terrace Bar' }
];

// access the elements
const foodCheckbox = document.getElementById('foodCheckbox');
const coffeeCheckbox = document.getElementById('coffeeCheckbox');
const wineCheckbox = document.getElementById('wineCheckbox');
const priceRangeMin = document.getElementById('priceRangeMin');
const priceRangeMax = document.getElementById('priceRangeMax');
const priceMinDisplay = document.getElementById('priceMin');
const priceMaxDisplay = document.getElementById('priceMax');
const starbucksRadio = document.getElementById('starbucksRadio');
const beautifulDuckRadio = document.getElementById('beautifulDuckRadio');
const terraceBarRadio = document.getElementById('terraceBarRadio');

// initialize the filters
let filters = {
    category: [],
    priceMin: 1,
    priceMax: 20,
    facility: [],
};

// update the price display
function updatePriceDisplay() {
    filters.priceMin = parseFloat(priceRangeMin.value);
    filters.priceMax = parseFloat(priceRangeMax.value);
    priceMinDisplay.textContent = filters.priceMin;
    priceMaxDisplay.textContent = filters.priceMax;
    applyFilters(); // reapply the filters
}

priceRangeMin.addEventListener('input', updatePriceDisplay);
priceRangeMax.addEventListener('input', updatePriceDisplay);

// add event listeners to the checkboxes and radio buttons
foodCheckbox.addEventListener('change', applyFilters);
coffeeCheckbox.addEventListener('change', applyFilters);
wineCheckbox.addEventListener('change', applyFilters);
starbucksRadio.addEventListener('change', applyFilters);
beautifulDuckRadio.addEventListener('change', applyFilters);
terraceBarRadio.addEventListener('change', applyFilters);

// Filter and display products based on filters
function applyFilters() {
    filters.category = [];
    filters.facility = [];

    if (foodCheckbox.checked) filters.category.push('Food');
    if (coffeeCheckbox.checked) filters.category.push('Coffee');
    if (wineCheckbox.checked) filters.category.push('Wine');

    if (starbucksRadio.checked) filters.facility.push('StarBucks Cafe');
    if (beautifulDuckRadio.checked) filters.facility.push('The Beautiful Duck Restaurant');
    if (terraceBarRadio.checked) filters.facility.push('Terrace Bar');

    const filteredProducts = allProducts.filter(product => {
        const categoryMatch = filters.category.length === 0 || filters.category.includes(product.category);
        const priceMatch = product.price >= filters.priceMin && product.price <= filters.priceMax;
        const facilityMatch = filters.facility.length === 0 || filters.facility.includes(product.facility);
        return categoryMatch && priceMatch && facilityMatch;
    });

    addProductCards(filteredProducts); 
}

// Dynamically create and add product cards to the page
function addProductCards(filteredProducts) {
    const container = document.getElementById('productsContainer');
    container.innerHTML = ''; // Empty the container to add a new product card

    filteredProducts.forEach(product => {
        const col = document.createElement('div');
        col.className = 'col';
        const card = `
        <div class="card h-100" data-category="${product.category}" data-price="${product.price}" data-facility="${product.facility}">
          <img src="static/images/${product.image}" class="card-img-top" alt="Product Image">
          <div class="card-body">
            <h5 class="card-title">${product.name}</h5>
            <p class="card-text">${product.category} - Price: £${product.price} - Size: ${product.size}</p>
          </div>
        </div>
      `;
        col.innerHTML = card;
        container.appendChild(col);
    });
}


updatePriceDisplay();
