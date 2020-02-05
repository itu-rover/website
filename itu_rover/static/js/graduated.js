function myFunction(x) {
    if(x.matches) {
        $("nav ul li").fadeOut();
        $("nav ul").fadeOut();
    }
}
$("#menu").click(function () {
            $("nav ul li").fadeToggle();
            $("nav ul").fadeToggle();
        });
        $("#dd-years").click(function () {
            $(".dd-years").fadeToggle()
        })

    var x = window.matchMedia("(max-width: 968px)")
    myFunction(x); // Call listener function at run time
    x.addListener(myFunction) // Attach listener function on state changes