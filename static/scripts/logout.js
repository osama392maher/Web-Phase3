function logout() {
    // Create a new form element
    var form = document.createElement("form");
    form.setAttribute("method", "post");
    form.setAttribute("action", "/logout/");

    // Regenerate the CSRF token
    var csrf_token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    var csrf = document.createElement("input");
    csrf.setAttribute("type", "hidden");
    csrf.setAttribute("name", "csrfmiddlewaretoken");
    csrf.setAttribute("value", csrf_token);
    form.appendChild(csrf);

    // Submit the form
    document.body.appendChild(form);
    form.submit();
}