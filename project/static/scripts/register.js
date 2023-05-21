// Get the form elements
const usernameInput = document.getElementById("username");
const passwordInput = document.getElementById("password");
const registerForm = document.getElementById("addStudentForm");

// Function to validate input fields
function validateFields() {
    const username = usernameInput.value.trim();
    const password = passwordInput.value.trim();
    
    // Check if input fields are not empty
    if (username === "" || password === "") {
        alert("Please fill all fields.");
        return false;
    }
    
    // TODO: Implement further validation logic as needed
    
    return true;
}

// Add event listener to the form submit button
registerForm.addEventListener("submit", (event) => {
    event.preventDefault();
    
    if (validateFields()) {
        const username = usernameInput.value.trim();
        const password = passwordInput.value.trim();
        
        // Check if admin with same username already exists
        const admins = JSON.parse(localStorage.getItem("admins")) || [];
        if (admins.find(admin => admin.username === username)) {
            alert("Admin with same username already exists.");
            return;
        }
        
        // Save admin to local storage
        admins.push({ username, password });
        localStorage.setItem("admins", JSON.stringify(admins));
        
        alert("Admin registered successfully!");
        
        // Clear input fields
        usernameInput.value = "";
        passwordInput.value = "";
    }
});