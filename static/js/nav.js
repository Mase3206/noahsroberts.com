// Make sure this matches the duration of the animation.
const overlap = 0.6;
const cssFadeDuration = 200;
const duration = cssFadeDuration * (1 - overlap);

$('.navbar-burger').click(function() {
  var $navbarMenu = $('#navbarMenu');
	var $below = $('#hiddenBelowNavmenu');

	if ($navbarMenu.hasClass('is-active')) {
		$navbarMenu.removeClass('fadeIn').addClass('fadeOut');
		$below.removeClass('fadeOut').addClass('fadeIn');

		setTimeout(function() {
			$navbarMenu.removeClass('is-active');
			$below.removeClass('is-hidden');
		}, duration);
	} else {
		$navbarMenu.removeClass('fadeOut').addClass('fadeIn');
		$below.removeClass('fadeIn').addClass('fadeOut');

		setTimeout(function() {
			$below.addClass('is-hidden');
			$navbarMenu.addClass('is-active');
		}, duration);
	}

	$('navbar-burger').toggleClass('is-active');
});

const mobileThreshhold = 1024;

function navSwitch() {
	if ($(this).width() >= mobileThreshhold) {
		console.log('desktop');
	  $('#navbarMenu').addClass('is-active').removeClass('fadeIn fadeOut');
		$('#hiddenBelowNavmenu').removeClass('is-hidden fadeIn fadeOut');
		$('navbar-burger').removeClass('is-active');
	} else {
		console.log('mobile');
		$('#navbarMenu').removeClass('is-active');
	}
}

var resizeTimer;
$(window).on('resize', function() {
	clearTimeout(resizeTimer);
	resizeTimer = setTimeout(navSwitch(), 250);
});
$(document).ready(navSwitch());