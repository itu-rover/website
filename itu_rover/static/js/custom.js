
console.log("1 loggggggggggg")

//  MENU SIZING FOR MOBILE

var x = window.matchMedia("(max-width: 968px)")


  if (x.matches) { // If media query matches

    // MOBILE

      function openNav() {
        document.getElementById("navbar-side").style.width = "80%";
      }

      function closeNav() {
        document.getElementById("navbar-side").style.width = "0";
      }
  } else {

    // PC

      function openNav() {
        document.getElementById("navbar-side").style.width = "30%";
      }

      function closeNav() {
        document.getElementById("navbar-side").style.width = "0";
      }
  }

  console.log("2 loggggggggggg")

         $(window).scroll(function () {
            if ($(window).scrollTop() > 100){
                $('.black-trans').fadeIn(400);
            }
            else {
                $('.black-trans').fadeOut(400);
            }
        })
console.log("3 loggggggggggg")
