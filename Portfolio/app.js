// Get the current year and update the footer
var currentYear = new Date().getFullYear();
document.getElementById("current-year").innerHTML = "© My Portfolio " + currentYear ;

// Function to reveal elements on the first page
function revealFirstPage() {
    var reveals = document.querySelectorAll('.reveal');
    var revealDelay = 100; // Adjust this value to set the delay between each element's appearance
  
    for (var i = 0; i < reveals.length; i++) {
      (function (index) {
        setTimeout(function () {
          reveals[index].classList.add('active');
        }, revealDelay * index);
      })(i);
    }
  }
  
  // Check if elements with class 'reveal' are present on the first page
  var firstPageReveals = document.querySelectorAll('.reveal');
  if (firstPageReveals.length > 0) {
    revealFirstPage();
  }
  
  // Function to reveal elements on subsequent pages as the user scrolls
  function revealOnScroll() {
    var reveals = document.querySelectorAll('.reveal');
    var revealPoint = 150;
  
    for (var i = 0; i < reveals.length; i++) {
      var windowHeight = window.innerHeight;
      var revealTop = reveals[i].getBoundingClientRect().top;
  
      if (revealTop < windowHeight - revealPoint) {
        reveals[i].classList.add('active');
      } else {
        reveals[i].classList.remove('active');
      }
    }
  }
  
  // Add a scroll event listener for subsequent pages
  window.addEventListener('scroll', revealOnScroll);