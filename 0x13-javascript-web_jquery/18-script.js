let button = 'DIV#toggle_header';
$(button).ready(function () {
  $(button).addClass('red');
});
$(button).click(function ToggleClass () {
  if ($(button).hasClass('red')) {
    $(button).addClass('green');
    $(button).removeClass('red');
  } else {
    $(button).addClass('red');
    $(button).removeClass('green');
  }
});
