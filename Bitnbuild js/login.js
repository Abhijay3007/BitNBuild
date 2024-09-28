document.getElementById('loginForm').addEventListener('submit', async function(event) {
    event.preventDefault(); // Prevent the form from submitting

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const message = document.getElementById('loginMessage');

    try {
        const response = await fetch('/api/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
        });

        const data = await response.json();

        if (response.ok) {
            message.style.color = 'green';
            message.textContent = 'Login successful!';
            // Redirect or perform further actions here
        } else {
            message.style.color = 'red';
            message.textContent = data.message || 'Wrong email or password.';
        }
    } catch (error) {
        message.style.color = 'red';
        message.textContent = 'An error occurred. Please try again.';
        console.error('Error:', error);
    }
});
