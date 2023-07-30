document.addEventListener("DOMContentLoaded", function () {
    const slides = document.querySelector(".slides");
    const slideWidth = slides.querySelector("img").clientWidth;
    let currentPosition = 0;
  
    // Function to move to the next slide
    function nextSlide() {
      currentPosition -= slideWidth;
      if (currentPosition < -slideWidth * (slides.children.length - 1)) {
        currentPosition = 0;
      }
      slides.style.transform = `translateX(${currentPosition}px)`;
    }
  
    // Function to start the automatic carousel
    function startCarousel() {
      setInterval(() => {
        nextSlide();
      }, 5000); // Change slide every 5 seconds (5000 milliseconds)
    }
  
    startCarousel(); // Start the automatic carousel when the page loads
  });
  