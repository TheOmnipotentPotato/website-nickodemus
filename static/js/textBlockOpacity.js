// When the user scrolls the page, execute myFunction 
window.onscroll = function() {myFunction()};

function myFunction() {
  var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
  var height = 1350 - document.documentElement.clientHeight;
  var scrolled = 100 - ((winScroll / height) * 100);
  document.getElementById("home-text-block").style.opacity = scrolled + "%";
}
