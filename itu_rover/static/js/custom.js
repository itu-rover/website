$("#egg-toggle").click(function() {
  $("#egg-index").toggleClass("hidden");
});

$("[data-toggle=popover]").popover({html:true});
$(function () {
  $('[data-toggle="popover"]').popover()
})
jQuery('row').bind('click', function(e) {
  if(jQuery(e.target).closest('.navbar').length == 0) {
    // click happened outside of .navbar, so hide
    var opened = jQuery('.navbar-collapse').hasClass('collapse in');
    if ( opened === true ) {
      jQuery('.navbar-collapse').collapse('hide');
    }
  }
});
