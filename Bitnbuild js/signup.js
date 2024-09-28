// Attach an event listener to the signup form
document.getElementById('signupForm').onsubmit = async function (e) {
    // Prevent the default form submission
    e.preventDefault();

    // Get the values from the form inputs
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Send the form data to the server using Fetch API
    const response = await fetch('/signup', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            username: username,
            email: email,
            password: password
        })
    });

    // Handle the server's response
    const result = await response.json();

    // Get the element where the status message will be shown
    const statusMessage = document.getElementById('statusMessage');

    if (response.status === 200) {
        // If the signup was successful, display a success message and redirect to index.html
        statusMessage.textContent = 'Signup successful! Redirecting to homepage...';
        statusMessage.style.color = 'green';
        setTimeout(() => {
            window.location.href = 'index.html'; // Redirect to homepage after 2 seconds
        }, 2000);
    } else {
        // If there was an error, display an error message
        statusMessage.textContent = result.message || 'An error occurred during signup.';
        statusMessage.style.color = 'red';
    }
};