// Login button handler
document.getElementById('loginBtn').onclick = function() {
    const email = document.getElementById('Email').value;
    const password = document.getElementById('password').value;

    // Basic validation for empty fields
    if (email === "" || password === "") {
        alert("Please enter both email and password.");
        return;
    }

    // You can add further logic here (e.g., send a request to the server to validate credentials)

    // For now, redirect to the dashboard if the form is filled
    window.location.href = 'dashboard.html';  // Redirect to the dashboard page
};

// Sign Up button handler
document.getElementById('signupBtn').onclick = function() {
    // Redirect to the signup page
    window.location.href = 'signup.html';
};