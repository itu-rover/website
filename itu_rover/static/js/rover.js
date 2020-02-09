$(document).ready(function(){

// ---------------With these functions below, page goes RIGHT and LEFT with buttons-----------

    function myFunction(x) {

        // MAX-WIDTH: 968px
    if (x.matches) { // If media query matches
        $("#left-btn").click(function() {
            $("#bg").animate({
                left: "0%",
            });/*

            $("#rover17").animate({
                left: "15%",
            });
            $("#rover18").animate({
                left: "112%",
            });
            $("#rover19").animate({
                left: "162%",
            });*/
            $("#rover17-prop, #rover17").fadeIn();
            $("#rover18-prop, #rover18").fadeOut();
            $("#rover19-prop, #rover19").fadeOut();
        });
        $("#middle-btn").click(function(){
            $("#bg").animate({
                left: "-10%",
            })/*
            $("#rover17").animate({
                left: "-100%",
            });
            $("#rover18").animate({
                left: "15%",
            });
            $("#rover19").animate({
                left: "112%",
            });*/
            $("#rover17-prop, #rover17").fadeOut();
            $("#rover18-prop, #rover18").fadeIn();
            $("#rover19-prop, #rover19").fadeOut();
          });
        $("#right-btn").click(function(){
            $("#bg").animate({
                left: "-20%",
            });/*
            $("#rover17").animate({
                left: "-200%",
            });
            $("#rover18").animate({
                left: "-100%",
            });
            $("#rover19").animate({
                left: "15%",
            });*/

            $("#rover17-prop, #rover17").fadeOut();
            $("#rover18-prop, #rover18").fadeOut();
            $("#rover19-prop, #rover19").fadeIn();
        });

        // PC DISPLAY

    } else {
            $("#left-btn").click(function(){
        $("#bg").animate({
            left: "0%",
        });/*

        $("#rover17").animate({
            left: "55%",
        });
        $("#rover18").animate({
            left: "100%",
        });
        $("#rover19").animate({
            left: "150%",
        });*/

        $("#rover17-prop, #rover17").fadeIn();
        $("#rover18-prop, #rover18").fadeOut();
        $("#rover19-prop, #rover19").fadeOut();
    });


      $("#middle-btn").click(function(){
        $("#bg").animate({
            left: "-10%",
        })/*
        $("#rover17").animate({
            left: "-50%",
        });
        $("#rover18").animate({
            left: "55%",
        });
        $("#rover19").animate({
            left: "100%",
        });*/

        $("#rover17-prop, #rover17").fadeOut();
        $("#rover18-prop, #rover18").fadeIn();
        $("#rover19-prop, #rover19").fadeOut();
      });


      $("#right-btn").click(function(){
        $("#bg").animate({
            left: "-20%",
        });/*
        $("#rover17").animate({
            left: "-100%",
        });
        $("#rover18").animate({
            left: "-50%",
        });
        $("#rover19").animate({
            left: "55%",
        });*/

        $("#rover17-prop, #rover17").fadeOut();
        $("#rover18-prop, #rover18").fadeOut();
        $("#rover19-prop, #rover19").fadeIn();
      });

  }
}

  var x = window.matchMedia("(max-width: 968px)")
    myFunction(x); // Call listener function at run time
    x.addListener(myFunction) // Attach listener function on state changes

});