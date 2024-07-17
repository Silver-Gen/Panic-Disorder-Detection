const form = document.querySelector('form');
const inputs = form.querySelectorAll('input[type="number"]');

form.addEventListener('submit', (event) => {
  for (const input of inputs) {
    if (input.value === '') {
      alert('Please fill in all fields');
      event.preventDefault();
      return;
    }
  }
});
