// // Get the table body element
// const tableBody = document.getElementById('student-table-body');

// // Retrieve student data from local storage
// const students = JSON.parse(localStorage.getItem('students'));

// // Loop through the students and create table rows
// students.forEach((student) => {
//   const row = tableBody.insertRow();

//   // Insert student data into table cells
//   row.insertCell().innerHTML = student.name;
//   row.insertCell().innerHTML = student.id;
//   row.insertCell().innerHTML = student.level;
//   row.insertCell().innerHTML = student.status;
//   row.insertCell().innerHTML = student.date;
//   row.insertCell().innerHTML = student.gpa;
//   row.insertCell().innerHTML = student.gender;
//   row.insertCell().innerHTML = student.email;
//   row.insertCell().innerHTML = student.department;
//   row.insertCell().innerHTML = student.phone;
//   row.insertCell().innerHTML = `<a href="EditStudentsPage.html?id=${student.id}" class="edit">&ensp; Edit &ensp;</a>`;
// });


// // Get the table body element
// const tableBody = document.getElementById('student-table-body');

// // Retrieve student data from local storage
// const students = JSON.parse(localStorage.getItem('students'));

// // Loop through the students and create table rows
// students.forEach((student) => {
//   const row = tableBody.insertRow();

// // Insert student data into table cells
//   row.insertCell().innerHTML = student.name;
//   row.insertCell().innerHTML = student.id;
//   row.insertCell().innerHTML = student.level;
//   row.insertCell().innerHTML = student.status;
//   row.insertCell().innerHTML = student.date;
//   row.insertCell().innerHTML = student.gpa;
//   row.insertCell().innerHTML = student.gender;
//   row.insertCell().innerHTML = student.email;
//   row.insertCell().innerHTML = student.department;
//   row.insertCell().innerHTML = student.phone;
//   row.insertCell().innerHTML = `<a href="EditStudentsPage.html?id=${student.id}" class="edit">&ensp; Edit &ensp;</a>`;
// });

// // Add search functionality
// const searchInput = document.querySelector('.search');
// const tableRows = document.querySelectorAll('#student-table-body tr');

// searchInput.addEventListener('input', () => {
//   const searchText = searchInput.value.toLowerCase();

//   // Loop through each row of the table body
//   tableRows.forEach((row, index) => {
//     // Skip the first row (table header)
//     if (index === 0) return;

//     const name = row.cells[0].textContent.toLowerCase();

//     // If the row's name matches the search text, show it
//     if (name.startsWith(searchText)) {
//       row.style.display = '';
//     } else {
//       // Otherwise, hide the row
//       row.style.display = 'none';
//     }
//   });
// });

// Get the table body element
const tableBody = document.getElementById('student-table-body');

// Retrieve student data from local storage
const students = JSON.parse(localStorage.getItem('students'));

// Loop through the students and create table rows
students.forEach((student) => {
  const row = tableBody.insertRow();

  // Insert student data into table cells
  row.insertCell().innerHTML = student.name;
  row.insertCell().innerHTML = student.id;
  row.insertCell().innerHTML = student.level;
  row.insertCell().innerHTML = student.status;
  row.insertCell().innerHTML = student.date;
  row.insertCell().innerHTML = student.gpa;
  row.insertCell().innerHTML = student.gender;
  row.insertCell().innerHTML = student.email;
  row.insertCell().innerHTML = student.department;
  row.insertCell().innerHTML = student.phone;
  row.insertCell().innerHTML = `<a id = "assign" href = "department?id=${student.id}" class="edit">&ensp; Assign Department &ensp;</>`;
});

const assignLink = document.getElementById('assign');



// Add search functionality
const searchInput = document.querySelector('.search');
const searchOption = document.querySelector('.search-option');
const tableRows = document.querySelectorAll('#student-table-body tr');

searchInput.addEventListener('input', () => {
  const searchText = searchInput.value.toLowerCase();
  const searchType = searchOption.value;

  // Loop through each row of the table body
  tableRows.forEach((row, index) => {
    // Skip the first row (table header)
    if (index === 0) return;

    const searchValue = row.cells[searchType].textContent.toLowerCase();

    // If the row's search value matches the search text, show it
    if (searchValue.startsWith(searchText)) {
      row.style.display = '';
    } else {
      // Otherwise, hide the row
      row.style.display = 'none';
    }
  });
});

// Add change event to the search option dropdown
searchOption.addEventListener('change', () => {
  searchInput.value = ''; // Clear the search input
});