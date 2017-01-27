var initialize = function(){
  console.log('initialize is called');
  $('input[name="text"]').on('keypress', function(){
    $('.has-error').hide();
  });
}
