// Get the student ID from the query string
const urlParams = new URLSearchParams(window.location.search);
const studentId = urlParams.get('id');

// edit the student data

const saveBtn = document.getElementById('save-btn');

saveBtn.addEventListener('click', () => {

  if (!validateForm()) {
    return;
  }

  // Get the updated student data from the form
  const updatedStudent = {
    name: nameInput.value,
    id: idInput.value,
    level: levelInput.value,
    status: statusSelect.value,
    date: dateInput.value,
    department: departmentSelect.value,
    gpa: gpaInput.value,
    email: emailInput.value,
    gender: genderSelect.value,
    phone: phoneInput.value
  };

  // Send the AJAX request to update the student data
  const xhr = new XMLHttpRequest();
  xhr.open('POST', `/EditStudent/${studentId}/`, true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      alert("Student data has been updated successfully");
      // Redirect the user back to the view all students page
      window.location.href = "viewStudents";
    }
  };
  xhr.send(JSON.stringify(updatedStudent));
});

// delete the student data

const deleteBtn = document.getElementById('del-btn');

deleteBtn.addEventListener('click', () => {
  
  const confirmed = confirm("Are you sure you want to delete this student?");
  
  if (!confirmed) {
    return;
  }

  // Send the AJAX request to delete the student data
  const xhr = new XMLHttpRequest();
  xhr.open('POST', '/deleteStudent/', true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      alert("Student has been deleted successfully");
      // Redirect the user back to the view all students page
      window.location.href = "viewStudents";
    }
  };
  xhr.send(JSON.stringify({ studentId: studentId }));
});

function validateForm() {
  // Get the form fields
  const name = nameInput.value.trim();
  const id = idInput.value.trim();
  const level = levelInput.value.trim();
  const status = statusSelect.value.trim();
  const date = dateInput.value.trim();
  const department = departmentSelect.value.trim();
  const gpa = gpaInput.value.trim();
  const email = emailInput.value.trim();
  const gender = genderSelect.value.trim();
  const phone = phoneInput.value.trim();

  // Validate form data
  if (nameInput.value.trim() === '') {
    alert('Please enter a name.');
    return false;
  }

  if (emailInput.value.trim() === '' || !/^\S+@\S+\.\S+$/.test(emailInput.value)) {
    alert('Please enter a valid email address.');
    return false;
  }

  if (idInput.value.trim() === '') {
    alert('Please enter an ID.');
    return false;
  }

  if (isNaN(levelInput.value) || levelInput.value < 1 || levelInput.value > 4) {
    alert('Please enter a level between 1 and 4.');
    return false;
  }

  if (isNaN(gpaInput.value) || gpaInput.value < 0 || gpaInput.value > 4) {
    alert('Please enter a GPA between 0 and 4.');
    return false;
  }

  if (!/^01[0125]\d{8}$/.test(phoneInput.value)) {
    alert('Please enter a valid phone number in the format 01X12345678.');
    return false;
  }

  if (new Date(dateInput.value) > new Date()) {
    alert('Please enter a date of birth that is not in the future.');
    return false;
  }

  return true;
}
