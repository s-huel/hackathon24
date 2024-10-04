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
                localStorage.setItem("data", result.data);  // Store the ID for use in other pages
                localStorage.setItem("role", result.role);  // Store the role for use in other pages
                
                if (result.role == "Teacher") {
                    window.location.href = "studentenlijst.html";
                }
                else window.location.href = "werkproces.html";
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
    console.log(localStorage.getItem("role"));
});
