// Login function
function login() {
    // Get entered username and password
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
  
    // Get admins from local storage
    const admins = JSON.parse(localStorage.getItem('admins'));
  
    // Check if entered username and password match any of the admins
    const matchedAdmin = admins.find(admin => admin.username === username && admin.password === password);
  
    if (matchedAdmin) {
      // Set logged in status in local storage
      localStorage.setItem('loggedIn', true);
  
      alert('Logged in successfully!');
  
      // Redirect to index
      window.location.href = '/';
    } else {
      alert('Invalid username or password');
    }
  }
  
  // Add event listener to login form submit button
  const loginForm = document.getElementById('addStudentForm');
  loginForm.addEventListener('submit', function(event) {
    event.preventDefault();
    login();
  });
  
  const loggedIn = localStorage.getItem("loggedIn");
  if (loggedIn === "true") {
      window.location.href = "/";

  }