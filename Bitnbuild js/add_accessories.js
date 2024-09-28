const form = document.getElementById('accessoryForm');

    // Add event listener for form submission
    form.addEventListener('submit', function(event) {
        // Prevent form from submitting automatically
        event.preventDefault();

        // Get form values
        const accessory = document.getElementById('accessory').value;
        const name = document.getElementById('name').value;
        const color = document.getElementById('color').value;
        const size = document.getElementById('size').value;
        const date = document.getElementById('date').value;

        // Validate form inputs
        if (!accessory || !name || !color || !size || !date) {
            alert('All fields are required.');
            return;
        }

        // Check if size is a positive number
        if (size <= 0) {
            alert('Size must be a positive number.');
            return;
        }

        // Confirm submission
        const confirmSubmit = confirm('Are you sure you want to submit the accessory details?');
        
        if (confirmSubmit) {
            // If confirmed, submit the form
            form.submit();
        }
    });