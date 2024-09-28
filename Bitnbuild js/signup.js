document.getElementById('signupForm').addEventListener('submit', async function(event) {
    event.preventDefault(); // Prevent the form from submitting

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const message = document.getElementById('signupMessage');

    try {
        const response = await fetch('/api/signup', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
        });

        const data = await response.json();

        if (response.ok) {
            message.style.color = 'green';
            message.textContent = 'Signup successful! You can now login.';
        } else {
            message.style.color = 'red';
            message.textContent = data.message || 'Signup failed.';
        }
    } catch (error) {
        message.style.color = 'red';
        message.textContent = 'An error occurred. Please try again.';
        console.error('Error:', error);
    }
});
