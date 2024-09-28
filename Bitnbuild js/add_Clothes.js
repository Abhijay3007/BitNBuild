document.getElementById('itemForm').onsubmit = function(e) {
    e.preventDefault();

    
    const brandName = document.getElementById('name').value;
    const color = document.getElementById('color').value;
    const size = document.getElementById('Size').value;
    const quantity = document.getElementById('quantity').value;
    const price = document.getElementById('price').value;
    const dateAdded = document.getElementById('Date').value;

    
    if (brandName === "" || size <= 0 || quantity <= 0 || price <= 0) {
        alert("Please fill out the form correctly.");
        return;
    }

  
    alert(`Item Information:
    Brand: ${brandName}
    Color: ${color}
    Size: ${size}
    Quantity: ${quantity}
    Price: $${price}
    Date Added: ${dateAdded}`);

   
};
