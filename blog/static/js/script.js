document.addEventListener("DOMContentLoaded", function () {
    // Login Form Validation
    const loginForm = document.querySelector(".login-box form");
    if (loginForm) {
        loginForm.addEventListener("submit", function (event) {
            clearErrors();
            const username = document.getElementById("username").value.trim();
            const password = document.getElementById("password").value.trim();
            let isValid = true;

            if (username === "") {
                displayError("username-error", "Username is required.");
                isValid = false;
            }
            if (password === "") {
                displayError("password-error", "Password is required.");
                isValid = false;
            }

            if (!isValid) {
                event.preventDefault();  // Prevent form submission if validation fails
            }
        });
    }

    // Sign-Up Form Validation
    const signUpForm = document.querySelector(".signup-box form");
    if (signUpForm) {
        signUpForm.addEventListener("submit", function (event) {
            clearErrors();
            const fullName = document.getElementById("fullname").value.trim();
            const email = document.getElementById("email").value.trim();
            const username = document.getElementById("username").value.trim();
            const password = document.getElementById("password").value.trim();
            let isValid = true;

            if (fullName === "") {
                displayError("fullname-error", "Full name is required.");
                isValid = false;
            }
            if (email === "" || !validateEmail(email)) {
                displayError("email-error", "Enter a valid email address.");
                isValid = false;
            }
            if (username === "") {
                displayError("username-error", "Username is required.");
                isValid = false;
            }
            if (password === "") {
                displayError("password-error", "Password is required.");
                isValid = false;
            }

            if (!isValid) {
                event.preventDefault();
            }
        });
    }

    // Display Error Message
    function displayError(elementId, message) {
        const errorElement = document.getElementById(elementId);
        if (errorElement) {
            errorElement.innerText = message;
            errorElement.style.display = "block";
        }
    }

    // Clear Previous Errors
    function clearErrors() {
        const errorMessages = document.querySelectorAll(".error-message");
        errorMessages.forEach(function (error) {
            error.innerText = "";
            error.style.display = "none";
        });
    }

    // Email Validation Function
    function validateEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }
});
