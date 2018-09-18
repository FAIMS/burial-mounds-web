"use strict";
$(".slider-for").slick({
  slidesToShow: 1,
  slidesToScroll: 3,
  arrows: false,
  fade: true,

  asNavFor: ".slider-nav"
});
$(".slider-nav").slick({
  slidesToShow: 3,
  slidesToScroll: 3,
  arrows: true,

  asNavFor: ".slider-for",

  focusOnSelect: true,
  variableWidth: false,
  responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 3,
        infinite: true
      }
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2
      }
    }
    // You can unslick at a given breakpoint now by adding:
    // settings: "unslick"
    // instead of a settings object
  ]
});

$("a[data-slide]").click(function(e) {
  e.preventDefault();
  var slideno = $(this).data("slide");
  $(".slider-nav").slick("slickGoTo", slideno - 1);
});
