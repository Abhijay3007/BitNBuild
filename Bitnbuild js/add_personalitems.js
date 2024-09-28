// Attach event listener to the form for when it is submitted
document.querySelector('form').onsubmit = function(e) {
    // Prevent the form from being submitted to a server
    e.preventDefault();

    // Get form input values
    const name = document.getElementById('name').value;
    const description = document.getElementById('Description').value;
    const price = document.getElementById('price').value;

    // Basic validation to ensure all fields are filled
    if (name === '' || description === '' || price === '') {
        alert("Please fill in all the fields.");
        return;
    }

    // Convert price to a number for validation
    const priceValue = parseFloat(price);
    if (priceValue <= 0) {
        alert("Price should be a positive number.");
        return;
    }

    // Display summary dynamically in the browser console (you can display this in the UI if required)
    console.log(`Item Summary:
    Name: ${name}
    Description: ${description}
    Price: $${priceValue.toFixed(2)}
    `);

    // Dynamic message based on price value
    if (priceValue > 1000) {
        alert("This item is expensive!");
    } else if (priceValue < 20) {
        alert("This is a budget-friendly item.");
    } else {
        alert("This item is reasonably priced.");
    }

    // You can proceed with submitting the form data to a server using AJAX or Fetch if needed.
};