(function ($) {
  $(document).ready(function () {

  ////////////////////////////////////////////////////

  ////////////////////////////////////////////////////
	// 03. Search Js

  if ($(".search-open-btn").length && $(".search-close-btn").length && $(".search__popup").length) {
    $(".search-open-btn").on("click", function () {
      $(".search__popup").addClass("search-opened");
    });
  
    $(".search-close-btn").on("click", function () {
      $(".search__popup").removeClass("search-opened");
    });
  }
  
//========== HEADER ACTIVE ENDS ============= //

//========== PRICING AREA ============= //

if ($("#ce-toggle").length) {
  $("#ce-toggle").on("click change", function () {
    $(".plan-toggle-wrap").toggleClass("active");

    if ($(this).is(":checked")) {
      $(".tab-content #yearly").hide();
      $(".tab-content #monthly").show();
    } else {
      $(".tab-content #yearly").show();
      $(".tab-content #monthly").hide();
    }
  });
}

//========== MOBILE MENU STARTS ============= //
  var vlMenuWrap = $('.vl-mobile-menu-active > ul').clone();
  var vlSideMenu = $('.vl-offcanvas-menu nav');
  vlSideMenu.append(vlMenuWrap);
  if ($(vlSideMenu).find('.sub-menu, .vl-mega-menu').length != 0) {
    $(vlSideMenu).find('.sub-menu, .vl-mega-menu').parent().append('<button class="vl-menu-close"><i class="fas fa-chevron-right"></i></button>');
  }

  var sideMenuList = $('.vl-offcanvas-menu nav > ul > li button.vl-menu-close, .vl-offcanvas-menu nav > ul li.has-dropdown > a');
  $(sideMenuList).on('click', function (e) {
    console.log(e);
    e.preventDefault();
    if (!($(this).parent().hasClass('active'))) {
      $(this).parent().addClass('active');
      $(this).siblings('.sub-menu, .vl-mega-menu').slideDown();
    } else {
      $(this).siblings('.sub-menu, .vl-mega-menu').slideUp();
      $(this).parent().removeClass('active');
    }
  });


  if ($(".vl-offcanvas-toggle").length && $(".vl-offcanvas").length && $(".vl-offcanvas-overlay").length) {
    $(".vl-offcanvas-toggle").on('click', function () {
      $(".vl-offcanvas").addClass("vl-offcanvas-open");
      $(".vl-offcanvas-overlay").addClass("vl-offcanvas-overlay-open");
    });
  
    $(".vl-offcanvas-close-toggle, .vl-offcanvas-overlay").on('click', function () {
      $(".vl-offcanvas").removeClass("vl-offcanvas-open");
      $(".vl-offcanvas-overlay").removeClass("vl-offcanvas-overlay-open");
    });
  }
  

//========== MOBILE MENU ENDS ============= //

// ===== work 4 hover effect ====

if ($('.cs_hover_active').length) {
  $('.cs_hover_active').on('mouseenter', function () {
    $(this).addClass('active').siblings().removeClass('active');
  });
}


    {
      function animateElements() {
        $('.progressbar').each(function () {
          var elementPos = $(this).offset().top;
          var topOfWindow = $(window).scrollTop();
          var percent = $(this).find('.circle').attr('data-percent');
          var percentage = parseInt(percent, 10) / parseInt(100, 10);
          var animate = $(this).data('animate');
          if (elementPos < topOfWindow + $(window).height() - 10 && !animate) {
            $(this).data('animate', true);
            $(this).find('.circle').circleProgress({
              startAngle: -Math.PI / 2,
              value: percent / 100,
              size: 80,
              thickness: 5,
              emptyFill: "#E7E6F1",
              fill: {
                color: '#0778F9'
              }
            }).on('circle-animation-progress', function (event, progress, stepValue) {
              $(this).find('div').text((stepValue*100).toFixed() + "%");
            }).stop();
          }
        });
      }
    
        // Show animated elements
        animateElements();
        $(window).scroll(animateElements);
        };

        //Video poppup
        if ($(".play-btn").length > 0) {
          $(".play-btn").magnificPopup({
            type: "iframe",
          });
        };

        //Aos animation active
        AOS.init({
          offset: 0,
          duration: 400,
          easing: "ease-in-out",
          anchorPlacement: "top-bottom",
          disable: "mobile",
          once: false,
        });

        // page-progress
        var progressPath = document.querySelector(".progress-wrap path");
        var pathLength = progressPath.getTotalLength();
        progressPath.style.transition = progressPath.style.WebkitTransition =
          "none";
        progressPath.style.strokeDasharray = pathLength + " " + pathLength;
        progressPath.style.strokeDashoffset = pathLength;
        progressPath.getBoundingClientRect();
        progressPath.style.transition = progressPath.style.WebkitTransition =
          "stroke-dashoffset 10ms linear";
        var updateProgress = function () {
          var scroll = $(window).scrollTop();
          var height = $(document).height() - $(window).height();
          var progress = pathLength - (scroll * pathLength) / height;
          progressPath.style.strokeDashoffset = progress;
        };
        updateProgress();
        $(window).scroll(updateProgress);
        var offset = 50;
        var duration = 550;
        jQuery(window).on("scroll", function () {
          if (jQuery(this).scrollTop() > offset) {
            jQuery(".progress-wrap").addClass("active-progress");
          } else {
            jQuery(".progress-wrap").removeClass("active-progress");
          }
        });
        jQuery(".progress-wrap").on("click", function (event) {
          event.preventDefault();
          jQuery("html, body").animate({ scrollTop: 0 }, duration);
          return false;
        });

        // Product colors - Accordion 1
        const colors = $(".accordion1 .accordion-item");
        if (colors.length) {
          colors.on("click", function () {
            $(".accordion1 .accordion-item").removeClass("active");
            $(this).addClass("active");
          });
        }

        // Product colors - Accordion 2
        const colors2 = $(".accordion2 .accordion-item");
        if (colors2.length) {
          colors2.on("click", function () {
            $(".accordion2 .accordion-item").removeClass("active");
            $(this).addClass("active");
          });
        }
          
  });

  if ($('.select-nice select').length) {
    $('.select-nice select').niceSelect();
  }  


  
if ($('.swiper-container').length) {
  new Swiper('.swiper-container', {
    loop: true,
    autoplay: {
      delay: 4000, // Auto slides every 4 seconds
    },
    slidesPerView: 1,
    spaceBetween: 20,
    pagination: {
      el: ".swiper-pagination",
      clickable: true, // Allow clicking on dots to navigate
    },
    speed: 1000,
    effect: "fade",
    breakpoints: {
      1920: {
        slidesPerView: 1,
        spaceBetween: 0
      },
      1028: {
        slidesPerView: 1,
        spaceBetween: 30
      },
      480: {
        slidesPerView: 1,
        spaceBetween: 10
      }
    }
  });
}

if ($('.case1-sliders').length) {
  const swiper = new Swiper(".case1-sliders", {
    loop: true,
    spaceBetween: 20,
    autoplay: {
      delay: 0,
    },
    speed: 4000,
    navigation: {
      nextEl: '.case1-next',
      prevEl: '.case1-prev',
    },

    breakpoints: {
      640: {
        slidesPerView: 1,
        spaceBetween: 20
      },
      767: {
        slidesPerView: 2,
        spaceBetween: 20
      },
      1024: {
        slidesPerView: 3,
        spaceBetween: 20
      }
    },
  });
}

if ($('.swiper-container2').length) {
  const swiper2 = new Swiper('.swiper-container2', {
    effect: "fade",
    loop: true,
    autoplay: {
      delay: 4000, // Auto slides every 4 seconds
    },
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
  });
}


if ($('.swiper-container5').length) {
  const swiper5 = new Swiper('.swiper-container5', {
    effect: "fade",
    loop: true,
    autoplay: {
      delay: 4000, // Auto slides every 4 seconds
    },
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
  });
}

if ($('.team2-slider').length) {
  const swiper6 = new Swiper('.team2-slider', {
    loop: true,
    autoplay: {
      delay: 300, // Auto slides every 0.3 seconds
    },
    speed: 4000,
    navigation: {
      nextEl: '.team2-next',
      prevEl: '.team2-prev',
    },
    breakpoints: {
      640: {
        slidesPerView: 1,
        spaceBetween: 20
      },
      767: {
        slidesPerView: 2,
        spaceBetween: 20
      },
      1024: {
        slidesPerView: 4,
        spaceBetween: 20
      }
    },
  });
}


if ($('.solutions4-slider').length) {
  const swiper8 = new Swiper('.solutions4-slider', {
    loop: true,
    spaceBetween: 30,
    autoplay: {
      delay: 4000,
    },
    navigation: {
      nextEl: '.solutions4-next',
      prevEl: '.solutions4-prev',
    },
    breakpoints: {
      640: {
        slidesPerView: 1,
        spaceBetween: 20
      },
      1024: {
        slidesPerView: 3,
        spaceBetween: 20
      }
    },
  });
}


if ($('.case5-slider').length) {
  const swiper10 = new Swiper('.case5-slider', {
    loop: true,
    centeredSlides: true,
    spaceBetween: 30,
    autoplay: {
      delay: 4000, // Auto slides every 4 seconds
    },
    navigation: {
      nextEl: '.case5-next',
      prevEl: '.case5-prev',
    },
    breakpoints: {
      768: {
        slidesPerView: 1,
        spaceBetween: 20
      },
      1024: {
        slidesPerView: 2.3,
        spaceBetween: 20
      }
    },
  });
}

  if ($('.case5grid6-slider').length) {
    const swiper10 = new Swiper('.case5grid6-slider', {
      loop: true,
      centeredSlides: true,
      spaceBetween: 30,
      autoplay: {
        delay: 4000,
      },
      navigation: {
        nextEl: '.case5-next',
        prevEl: '.case5-prev',
      },
      slidesPerView: 3,
      breakpoints: {
        768: {
          slidesPerView: 4,
          spaceBetween: 20
        },
        1024: {
          slidesPerView: 6,
          spaceBetween: 20
        }
      },
    });
  }


if ($('.team5-slider').length) {
  const swiper11 = new Swiper('.team5-slider', {
    loop: true,
    centeredSlides: true,
    spaceBetween: 30,
    autoplay: {
      delay: 4000, // Auto slides every 4 seconds
    },
    navigation: {
      nextEl: '.team5-next',
      prevEl: '.team5-prev',
    },
    breakpoints: {
      768: {
        slidesPerView: 1,
        spaceBetween: 20
      },
      1024: {
        slidesPerView: 3,
        spaceBetween: 20
      }
    },
  });
}


if ($('.case3-slider').length) {
  const swiper12 = new Swiper('.case3-slider', {
    loop: true,
    centeredSlides: true,
    spaceBetween: 30,
    autoplay: {
      delay: 4000, // Auto slides every 4 seconds
    },
    navigation: {
      nextEl: '.case3-next',
      prevEl: '.case3-prev',
    },
    breakpoints: {
      768: {
        slidesPerView: 1,
        spaceBetween: 20
      },
      1024: {
        slidesPerView: 3,
        spaceBetween: 20
      }
    },
  });
}

if ($('.tes4-slider').length) {
  const swiper9 = new Swiper(".tes4-slider", {
    loop: true,
    slidesPerView: 1,
    spaceBetween: 20,
    navigation: {
      nextEl: '.tes4-next',
      prevEl: '.tes4-prev',
    },
    autoplay: {
      delay: 4000, // Auto slides every 4 seconds
    },
    breakpoints: {
      640: {
        slidesPerView: 1,
        spaceBetween: 20
      },
      1024: {
        slidesPerView: 1,
        spaceBetween: 20
      }
    },
  });
}

if ($('.tes1-slider-area').length) {
  const swiper3 = new Swiper('.tes1-slider-area', {
    slidesPerView: 1,
    spaceBetween: 10,
    autoplay: {
      delay: 4000, // Auto slides every 4 seconds
    },
    pagination: {
      el: ".swiper-pagination2",
      clickable: true, // Allow clicking on dots to navigate
    },
    breakpoints: {
      640: {
        slidesPerView: 1,
        spaceBetween: 20,
      },
      768: {
        slidesPerView: 1,
        spaceBetween: 30,
      },
      1024: {
        slidesPerView: 1,
        spaceBetween: 40,
      },
    },
  });
}



if ($('.slider-galeria-thumbs').length && $('.slider-galeria').length) {
  const thumbSwiper = new Swiper('.slider-galeria-thumbs', {
    direction: 'vertical',
    slidesPerView: 4,
    spaceBetween: 10,
    watchSlidesProgress: true,
    watchSlidesVisibility: true,
    slideToClickedSlide: true,
    loop: true,
    autoplay: {
      delay: 300, // Auto slides every 0.3 seconds
    },
    speed: 4000,
  });

  const mainSwiper = new Swiper('.slider-galeria', {
    spaceBetween: 10,
    loop: true,
    autoplay: {
      delay: 300, // Auto slides every 0.3 seconds
    },
    speed: 4000,
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
    thumbs: {
      swiper: thumbSwiper,
    },
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
  });
}


//== Testimonial 3 ===
if ($('.swiper-thumb2').length && $('.swiper-testimonial-2').length) {
  var swiper3 = new Swiper(".swiper-thumb2", {
    spaceBetween: 10,
    slidesPerView: 6,
    freeMode: true,
    watchSlidesProgress: true,
    autoplay: {
      delay: 2500, // Auto slides every 2.5 seconds
      disableOnInteraction: false,
    },
  });

  var swiper4 = new Swiper(".swiper-testimonial-2", {
    spaceBetween: 10,
    loop: true,
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    autoplay: {
      delay: 2500, // Auto slides every 2.5 seconds
      disableOnInteraction: false,
    },
    thumbs: {
      swiper: swiper3,
    },
  });
}

            
$(window).on("load", function () {
  if ($(".preloader").length) {
    setTimeout(function () {
      $(".preloader").fadeToggle();
    }, 500);
  }
});

})(jQuery);


// 3d time 

let lastScroll = 0; // Store the last scroll position
const header = document.getElementById('vl-header-sticky');

window.addEventListener('scroll', function() {
  const currentScroll = window.scrollY;

  if (currentScroll <= 150) {
    // At the top of the page, always show the header
    header.classList.remove('header-sticky');
    header.classList.remove('hide'); // Ensure the header is not hidden
    return;
  }

  if (currentScroll > lastScroll && header.classList.contains('header-sticky')) {
    // Scrolling down: show the header
    header.classList.remove('header-sticky');
    header.classList.add('hide'); // Add the 'hide' class
  } else if (currentScroll < lastScroll && !header.classList.contains('header-sticky')) {
    // Scrolling up: hide the header
    header.classList.add('header-sticky');
    header.classList.remove('hide'); // Remove the 'hide' class
  }

  lastScroll = currentScroll; // Update the last scroll position
});

 // === swiper slider area ===

//---- hero slider 1 ----


document.addEventListener('DOMContentLoaded', function () {
  if (document.querySelector('.logisticsSwiper')) {
    const swiper7 = new Swiper('.logisticsSwiper', {
      effect: "fade",
      autoplay: {
        delay: 300, // Auto slides every 0.3 seconds
      },
      speed: 4000,
      navigation: {
        nextEl: '.swiper-button-next3',
        prevEl: '.swiper-button-prev3'
      }
    });

    const paginationButtons = document.querySelectorAll('.pagination-btn');

    paginationButtons.forEach((btn, index) => {
      btn.addEventListener('click', () => {
        swiper7.slideToLoop(index); // Go to real slide
        setActivePagination(index);
      });
    });

    swiper7.on('slideChange', () => {
      setActivePagination(swiper7.realIndex);
    });

    function setActivePagination(activeIndex) {
      paginationButtons.forEach((btn, idx) => {
        btn.classList.toggle('active', idx === activeIndex);
      });
    }
  }
});

//=== form balance slider ====

const slider = document.getElementById('balance-slider');
const selectedValue = document.getElementById('selectedValue');

if (slider && selectedValue) {
  // Function to update the background gradient
  function updateSliderBackground() {
    const value = slider.value;
    const max = slider.max;
    const percentage = (value / max) * 100;
    slider.style.background = `linear-gradient(to right, red ${percentage}%, #e0e0e0 ${percentage}%)`;
  }

  // Event listener for slider input
  slider.addEventListener('input', function () {
    selectedValue.textContent = this.value;
    updateSliderBackground();
  });

  // Initialize the slider background on page load
  updateSliderBackground();
}

const slider2 = document.getElementById('balance-slider2');
const selectedValue2 = document.getElementById('selectedValue2');

if (slider2 && selectedValue2) {
  // Function to update the background gradient
  function updateSliderBackground() {
    const value = slider2.value;
    const max = slider2.max;
    const percentage = (value / max) * 100;
    slider2.style.background = `linear-gradient(to right, red ${percentage}%, #e0e0e0 ${percentage}%)`;
  }

  // Event listener for slider input
  slider2.addEventListener('input', function () {
    selectedValue2.textContent = this.value;
    updateSliderBackground();
  });

  // Initialize the slider background on page load
  updateSliderBackground();
}
