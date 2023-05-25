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