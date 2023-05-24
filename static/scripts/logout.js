
const loggedIn = localStorage.getItem("loggedIn");
if (loggedIn !== "true") {
    alert('You must be logged in to view this page.');
    window.location.href = "/login";
}

// Get the logout link from the navigation bar
const logoutLink = document.querySelector('nav #logout');

// Add a click event listener to the logout link
logoutLink.addEventListener('click', (event) => {
    // Prevent the default behavior of the link (i.e. following the link)
    event.preventDefault();

    localStorage.setItem('loggedIn', false);

    // Redirect the user to the login pageß
    window.location.href = '/login';

});
