var levelInput = document.getElementById("level");
var departmentSelect = document.getElementById("de");

levelInput.addEventListener("change", function () {
    if (levelInput.value < 3) {
        departmentSelect.value = "NO";
        departmentSelect.disabled = true;
    } else {
        departmentSelect.disabled = false;
    }
});


