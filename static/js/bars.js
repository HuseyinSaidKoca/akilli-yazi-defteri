const bars = document.querySelectorAll('.bar');
const progress = document.querySelectorAll('.progress');

bars.forEach((bar, index) => {
  const randomWidth = Math.floor((Math.random() * 65) + 10);
  bar.style.width = `${randomWidth}%`;

})
