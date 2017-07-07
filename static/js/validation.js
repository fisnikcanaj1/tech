$(document).ready(function() {
  //$(".main-form").fadeOut('slow/400/fast');

  $("input[type='radio']").on('click', function(event) {

    var radioValue = $("input[name='confidential']:checked").val();
    if(radioValue === "yes"){
    //  $(".main-form").show('slow/400/fast');
      $("#telephone-no").prop("disabled", false);
    }
    else{
    //  $(".main-form").fadeOut('slow/400/fast');
      $("#telephone-no").prop("disabled", true);
    }

  });

});
