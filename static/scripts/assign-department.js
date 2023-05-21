// Get the student ID from the query string
const urlParams = new URLSearchParams(window.location.search);
const studentId = urlParams.get('id');

// Retrieve student data from local storage
const students = JSON.parse(localStorage.getItem('students'));

// Find the student with the matching ID
const student = students.find((s) => s.id === studentId);

// Fill in the form with the student data
const nameInput = document.getElementById("name");
nameInput.value = student.name;

const idInput = document.getElementById("id");
idInput.value = student.id;

const departmentSelect = document.getElementById("de");
departmentSelect.value = student.department;

const saveBtn = document.getElementById('save-btn');

saveBtn.addEventListener('click', () => {

  // Check if student's level is 3 or 4 before updating department
  if (student.level === 3 || student.level === 4) {
    // Get the updated student data from the form
    const updatedStudent = {
      name: student.name,
      id: student.id,
      level : student.level,
      status : student.status,
      date : student.date,
      department: departmentSelect.value,
      gpa : student.gpa,
      email : student.email,
      gender : student.gender,
      phone : student.phone
    };
    // Find the index of the student with the matching ID
    const studentIndex = students.findIndex((s) => s.id === studentId);

    // Update the student data in the array
    students[studentIndex] = updatedStudent;

    // Save the updated student data back to local storage
    localStorage.setItem('students', JSON.stringify(students));

    alert("Department has been assigned successfully!");

    // Redirect the user back to the view all students page
    window.location.href = "assignDepartment";
  } else {
    alert("Cannot assign department for students below level 3.");
  }
});