const nav = document.getElementsByTagName("nav")[0];
window.addEventListener("scroll", function() {
    var navbar = document.getElementsByClassName('full-post-container')[0];
    if (window.scrollY > 10) {
      nav.style.transform = "translateY(-100%)";
    } else {
        nav.style.transform = "translateY(0)";
    }
  });