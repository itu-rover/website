$(document).ready(function(){
//$("#bg").css({left: "-30%"});

$("#bg").animate({width: "120%", left: "-10%", top: "-20%"}, 500, function(){});

// MENU icon for mobile

$("#menu").click(function () {
    $("nav ul li").fadeToggle();
    $("nav ul").fadeToggle();
});

if (window.location.href.indexOf("/eng/") > -1) {
    document.body.addEventListener('touchmove', function(e){ e.preventDefault(); });
    if(window.location.href.indexOf("127.0.0.1:8000/eng/past/20") > -1) {
    $("#first-btn").click(function () {
        $("#_1").animate({top: "0"});
        $("#_2").animate({top: "0"});
    });
    $("#second-btn").click(function () {
        $("#_1").animate({top: "-100%"});
        $("#_2").animate({top: "-100%"});
    });

} else {
    $("#first-btn").click(function () {
        $("#_1").animate({top: "0"});
        $("#_2").animate({top: "0"});
        $("#_3").animate({top: "0"});
        $("#_4").animate({top: "100%"});
        $("#_5").animate({top: "100%"});
        $("#_6").animate({top: "100%"});
    });
    $("#second-btn").click(function () {
        $("#_1").animate({top: "-100%"});
        $("#_2").animate({top: "-100%"});
        $("#_3").animate({top: "-100%"});
        $("#_4").animate({top: "0"});
        $("#_5").animate({top: "0"});
        $("#_6").animate({top: "0"});
    });
    $("#sponsors").click(function () {
        $("#_1").animate({top: "-100%"});
        $("#_2").animate({top: "-100%"});
        $("#_3").animate({top: "-100%"});
        $("#_4").animate({top: "0"});
        $("#_5").animate({top: "0"});
        $("#_6").animate({top: "0"});
    });

    $("#third-btn").click(function () {
        $("#_1").animate({top: "-200%"});
        $("#_2").animate({top: "-200%"});
        $("#_3").animate({top: "-200%"});
        $("#_4").animate({top: "-100%"});
        $("#_5").animate({top: "-100%"});
        $("#_6").animate({top: "-100%"});
    });
    $("#members").click(function () {
        $("#_1").animate({top: "-200%"});
        $("#_2").animate({top: "-200%"});
        $("#_3").animate({top: "-200%"});
        $("#_4").animate({top: "-100%"});
        $("#_5").animate({top: "-100%"});
        $("#_6").animate({top: "-100%"});
    });

    $("#fourth-btn").click(function () {
        $("#_1").animate({top: "-300%"});
        $("#_2").animate({top: "-300%"});
        $("#_3").animate({top: "-300%"});
        $("#_4").animate({top: "-200%"});
        $("#_5").animate({top: "-200%"});
        $("#_6").animate({top: "-200%"});
    });
    $("#faq").click(function () {
        $("#_1").animate({top: "-300%"});
        $("#_2").animate({top: "-300%"});
        $("#_3").animate({top: "-300%"});
        $("#_4").animate({top: "-200%"});
        $("#_5").animate({top: "-200%"});
        $("#_6").animate({top: "-200%"});
    });

    $("#fifth-btn").click(function () {
        $("#_1").animate({top: "-400%"});
        $("#_2").animate({top: "-400%"});
        $("#_3").animate({top: "-400%"});
        $("#_4").animate({top: "-300%"});
        $("#_5").animate({top: "-300%"});
        $("#_6").animate({top: "-300%"});
    });
    $("#rover").click(function () {
        $("#_1").animate({top: "-400%"});
        $("#_2").animate({top: "-400%"});
        $("#_3").animate({top: "-400%"});
        $("#_4").animate({top: "-300%"});
        $("#_5").animate({top: "-300%"});
        $("#_6").animate({top: "-300%"});
    });

    $("#sixth-btn").click(function () {
        $("#_1").animate({top: "-500%"});
        $("#_2").animate({top: "-500%"});
        $("#_3").animate({top: "-500%"});
        $("#_4").animate({top: "-400%"});
        $("#_5").animate({top: "-400%"});
        $("#_6").animate({top: "-400%"});
    });
    $("#about").click(function () {
        $("#_1").animate({top: "-500%"});
        $("#_2").animate({top: "-500%"});
        $("#_3").animate({top: "-500%"});
        $("#_4").animate({top: "-400%"});
        $("#_5").animate({top: "-400%"});
        $("#_6").animate({top: "-400%"});
    });
}
} else{
    if(window.location.href.indexOf("127.0.0.1:8000/gecmis/20") > -1) {
    $("#first-btn").click(function () {
        $("#_1").animate({top: "0"});
        $("#_2").animate({top: "0"});
    });
    $("#second-btn").click(function () {
        $("#_1").animate({top: "-100%"});
        $("#_2").animate({top: "-100%"});
    });

} else {
    $("#first-btn").click(function () {
        $("#_1").animate({top: "0"});
        $("#_2").animate({top: "0"});
        $("#_3").animate({top: "0"});
        $("#_4").animate({top: "100%"});
        $("#_5").animate({top: "100%"});
        $("#_6").animate({top: "100%"});
    });
    $("#second-btn").click(function () {
        $("#_1").animate({top: "-100%"});
        $("#_2").animate({top: "-100%"});
        $("#_3").animate({top: "-100%"});
        $("#_4").animate({top: "0"});
        $("#_5").animate({top: "0"});
        $("#_6").animate({top: "0"});
    });
    $("#sponsors").click(function () {
        $("#_1").animate({top: "-100%"});
        $("#_2").animate({top: "-100%"});
        $("#_3").animate({top: "-100%"});
        $("#_4").animate({top: "0"});
        $("#_5").animate({top: "0"});
        $("#_6").animate({top: "0"});
    });

    $("#third-btn").click(function () {
        $("#_1").animate({top: "-200%"});
        $("#_2").animate({top: "-200%"});
        $("#_3").animate({top: "-200%"});
        $("#_4").animate({top: "-100%"});
        $("#_5").animate({top: "-100%"});
        $("#_6").animate({top: "-100%"});
    });
    $("#members").click(function () {
        $("#_1").animate({top: "-200%"});
        $("#_2").animate({top: "-200%"});
        $("#_3").animate({top: "-200%"});
        $("#_4").animate({top: "-100%"});
        $("#_5").animate({top: "-100%"});
        $("#_6").animate({top: "-100%"});
    });

    $("#fourth-btn").click(function () {
        $("#_1").animate({top: "-300%"});
        $("#_2").animate({top: "-300%"});
        $("#_3").animate({top: "-300%"});
        $("#_4").animate({top: "-200%"});
        $("#_5").animate({top: "-200%"});
        $("#_6").animate({top: "-200%"});
    });
    $("#faq").click(function () {
        $("#_1").animate({top: "-300%"});
        $("#_2").animate({top: "-300%"});
        $("#_3").animate({top: "-300%"});
        $("#_4").animate({top: "-200%"});
        $("#_5").animate({top: "-200%"});
        $("#_6").animate({top: "-200%"});
    });

    $("#fifth-btn").click(function () {
        $("#_1").animate({top: "-400%"});
        $("#_2").animate({top: "-400%"});
        $("#_3").animate({top: "-400%"});
        $("#_4").animate({top: "-300%"});
        $("#_5").animate({top: "-300%"});
        $("#_6").animate({top: "-300%"});
    });
    $("#rover").click(function () {
        $("#_1").animate({top: "-400%"});
        $("#_2").animate({top: "-400%"});
        $("#_3").animate({top: "-400%"});
        $("#_4").animate({top: "-300%"});
        $("#_5").animate({top: "-300%"});
        $("#_6").animate({top: "-300%"});
    });

    $("#sixth-btn").click(function () {
        $("#_1").animate({top: "-500%"});
        $("#_2").animate({top: "-500%"});
        $("#_3").animate({top: "-500%"});
        $("#_4").animate({top: "-400%"});
        $("#_5").animate({top: "-400%"});
        $("#_6").animate({top: "-400%"});
    });
    $("#about").click(function () {
        $("#_1").animate({top: "-500%"});
        $("#_2").animate({top: "-500%"});
        $("#_3").animate({top: "-500%"});
        $("#_4").animate({top: "-400%"});
        $("#_5").animate({top: "-400%"});
        $("#_6").animate({top: "-400%"});
    });
}
}

});