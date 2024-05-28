document.addEventListener('DOMContentLoaded', function () {
  const foodLink = document.getElementById('foodLink');
  const retailLink = document.getElementById('retailLink');
  const foodContent = document.querySelectorAll('.food-content');
  const retailContent = document.querySelectorAll('.retail-content');

  // Initially hide all elements with the specified classes
  foodContent.forEach(element => {
    element.style.display = 'none';
  });

  // Add event listeners
  foodLink.addEventListener('click', () => {
    // Hide all retail-content elements
    retailContent.forEach(element => {
      element.style.display = 'none';
    });

    // Show all food-content elements
    foodContent.forEach(element => {
      element.style.display = 'block';
    });
  });

  retailLink.addEventListener('click', () => {
    // Hide all food-content elements
    foodContent.forEach(element => {
      element.style.display = 'none';
    });

    // Show all retail-content elements
    retailContent.forEach(element => {
      element.style.display = 'block';
    });
  });
});
