$(document).ready(function(){
//$("#bg").css({left: "-30%"});


if (window.location.href.indexOf("/eng/") > -1) {
    if(window.location.href.indexOf("/eng/past/20") > -1) {
    $("#first-btn").click(function () {
        $("#_1").animate({top: "0"});
        $("#_2").animate({top: "0"});
    });
    $("#second-btn").click(function () {
        $("#_1").animate({top: "-100%"});
        $("#_2").animate({top: "-100%"});
    });

} else {
    $("#sponsors").click(function () {
        $("#_1").animate({top: "-100%"});
        $("#_2").animate({top: "-100%"});
        $("#_3").animate({top: "-100%"});
        $("#_4").animate({top: "0"});
        $("#_5").animate({top: "0"});
        $("#_6").animate({top: "0"});
    });
    $("#members").click(function () {
        $("#_1").animate({top: "-200%"});
        $("#_2").animate({top: "-200%"});
        $("#_3").animate({top: "-200%"});
        $("#_4").animate({top: "-100%"});
        $("#_5").animate({top: "-100%"});
        $("#_6").animate({top: "-100%"});
    });
    $("#faq").click(function () {
        $("#_1").animate({top: "-300%"});
        $("#_2").animate({top: "-300%"});
        $("#_3").animate({top: "-300%"});
        $("#_4").animate({top: "-200%"});
        $("#_5").animate({top: "-200%"});
        $("#_6").animate({top: "-200%"});
    });
    $("#rover").click(function () {
        $("#_1").animate({top: "-400%"});
        $("#_2").animate({top: "-400%"});
        $("#_3").animate({top: "-400%"});
        $("#_4").animate({top: "-300%"});
        $("#_5").animate({top: "-300%"});
        $("#_6").animate({top: "-300%"});
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
    if(window.location.href.indexOf("/gecmis/20") > -1) {
    $("#first-btn").click(function () {
        $("#_1").animate({top: "0"});
        $("#_2").animate({top: "0"});
    });
    $("#second-btn").click(function () {
        $("#_1").animate({top: "-100%"});
        $("#_2").animate({top: "-100%"});
    });

} else {
    $("#sponsors").click(function () {
        $("#_1").animate({top: "-100%"});
        $("#_2").animate({top: "-100%"});
        $("#_3").animate({top: "-100%"});
        $("#_4").animate({top: "0"});
        $("#_5").animate({top: "0"});
        $("#_6").animate({top: "0"});
    });
    $("#members").click(function () {
        $("#_1").animate({top: "-200%"});
        $("#_2").animate({top: "-200%"});
        $("#_3").animate({top: "-200%"});
        $("#_4").animate({top: "-100%"});
        $("#_5").animate({top: "-100%"});
        $("#_6").animate({top: "-100%"});
    });
    $("#faq").click(function () {
        $("#_1").animate({top: "-300%"});
        $("#_2").animate({top: "-300%"});
        $("#_3").animate({top: "-300%"});
        $("#_4").animate({top: "-200%"});
        $("#_5").animate({top: "-200%"});
        $("#_6").animate({top: "-200%"});
    });
    $("#rover").click(function () {
        $("#_1").animate({top: "-400%"});
        $("#_2").animate({top: "-400%"});
        $("#_3").animate({top: "-400%"});
        $("#_4").animate({top: "-300%"});
        $("#_5").animate({top: "-300%"});
        $("#_6").animate({top: "-300%"});
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