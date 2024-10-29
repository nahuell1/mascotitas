(function($) {
  // Efectos "parallax"
  window.addEventListener("scroll", function(){
    let offset = window.pageYOffset;
    $("#parallax").css("backgroundPositionY", offset * -0.4+"px");
    $(".circuloRosa").css("margin-top", offset * -2+"px");
    $(".circuloAmarillo").css("margin-top", offset * -1.5+"px");
    $(".text_parallax").css("opacity",1 - offset * 0.005);
  })

  $(document).ready(function(){
      $(this).scrollTop(0);
  });

  // Navigation scrolls
  $(".navbar-nav li a").on('click', function(event) {
    $('.navbar-nav li').removeClass('active');
    $(this).closest('li').addClass('active');
    var $anchor = $(this);
    var nav = $($anchor.attr('href'));
    if (nav.length) {
      $('html, body').stop().animate({
        scrollTop: $($anchor.attr('href')).offset().top
      }, 1500, 'easeInOutExpo');

      event.preventDefault();
    }
  });
  $(".navbar-collapse a").on('click', function() {
    $(".navbar-collapse.collapse").removeClass('in');
  });

  // Add smooth scrolling to all links in navbar
  $("a.mouse-hover, a.get-quote").on('click', function(event) {
    var hash = this.hash;
    if (hash) {
      event.preventDefault();
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 1500, 'easeInOutExpo');
    }
  });
})(jQuery);
