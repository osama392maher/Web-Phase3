// Get the form and input fields
const form = document.getElementById('addStudentForm');
const nameInput = document.getElementById('name');
const ageInput = document.getElementById('date');
const gradeInput = document.getElementById('gpa');

// Add event listener for form submit
form.addEventListener('submit', (event) => {
  // Prevent the form from submitting
  event.preventDefault();

  // Check if the name field is empty
  if (nameInput.value.trim() === '') {
    // Display error message
    alert('Please enter a name');
    // Focus on the name field
    nameInput.focus();
    // Exit the function
    return;
  }

  // Check if the age field is empty
  if (ageInput.value.trim() === '') {
    // Display error message
    alert('Please enter a date of birth');
    // Focus on the age field
    ageInput.focus();
    // Exit the function
    return;
  }

  // Check if the grade field is empty
  if (gradeInput.value.trim() === '') {
    // Display error message
    alert('Please enter a GPA');
    // Focus on the grade field
    gradeInput.focus();
    // Exit the function
    return;
  }

  // Get the new student's information
  const name = document.querySelector('#name').value.trim();
  const id = document.querySelector('#id').value.trim();
  const level = document.querySelector('#level').value;
  const status = document.querySelector('#status').value;
  const date = document.querySelector('#date').value;
  const department = document.querySelector('#de').value;
  const gpa = document.querySelector('#gpa').value.trim();
  const email = document.querySelector('#email').value.trim();
  const gender = document.querySelector('#gender').value;
  const phone = document.querySelector('#phone').value.trim();

  // Check if the ID already exists in the list of students
  const students = JSON.parse(localStorage.getItem('students')) || [];
  const studentExists = students.some(student => student.id === id);
  if (studentExists) {
    alert('ID already exists');
    return;
  }

  // Add the new student to the list
  const student = {
    name,
    id,
    level,
    status,
    date,
    department,
    gpa,
    email,
    gender,
    phone
  };

  students.push(student);

  localStorage.setItem('students', JSON.stringify(students));

  alert('Student added successfully');
  window.location.href = "viewStudents";
});