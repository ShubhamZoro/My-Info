document.addEventListener("DOMContentLoaded", function() {
    const openFormBtn = document.getElementById("openFormBtn");
    const closeBtn = document.querySelector(".close-btn");
    const contactForm = document.getElementById("contactForm");
    const emailForm = document.getElementById("emailForm");

    openFormBtn.addEventListener("click", function() {
        contactForm.style.display = "block";
    });

    closeBtn.addEventListener("click", function() {
        contactForm.style.display = "none";
    });

    window.addEventListener("click", function(event) {
        if (event.target === contactForm) {
            contactForm.style.display = "none";
        }
    });

    emailForm.addEventListener("submit", function(event) {
        event.preventDefault();
        const name = document.getElementById("name").value;
        const email = document.getElementById("email").value;
        const message = document.getElementById("message").value;

        fetch('/send_email', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name, email, message })
        })
        .then(response => response.json())
        .then(data => {
            alert('Email sent successfully!');
            contactForm.style.display = "none"; // Hide the form after sending email
        })
        .catch(error => {
            console.error('Error sending email:', error);
            alert('Failed to send email.');
        });
    });
});