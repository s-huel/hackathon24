document.getElementById("login-form").addEventListener("submit", async function(event) {
    event.preventDefault(); // Prevent default form submission

    // Get form input values
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    try {
        // Make a fetch request to the FastAPI server
        const response = await fetch('http://localhost:8000/login?email=' + email + '&password=' + password, {
            method: 'GET',
        });

        // Parse the response
        if (response.ok) {
            const result = await response.json();

            // Assuming the result contains user data, store the ID in localStorage/sessionStorage
            if (result.data) {
                const userId = result.data[0];  // Assuming the first element is the user ID
                localStorage.setItem("userId", userId);  // Store the ID for use in other pages

                // Redirect to the home page
                window.location.href = "home.html";
            }
        } else {
            // Handle error responses
            const errorData = await response.json();
            alert("Login failed: " + errorData.detail);
        }
    } catch (error) {
        console.error("Error during fetch:", error);
        alert("Something went wrong. Please try again later.");
    }
});
