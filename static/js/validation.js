$(document).ready(function() {
  //$(".main-form").fadeOut('slow/400/fast');
  $("#radio-error").html("Please answer question of confidentiality before start with form.");
  $("input[name='confidential']").on('click', function(event) {

    var radioValue = $("input[name='confidential']:checked").val();

    if(radioValue === "yes"){
    //$(".main-form").show('slow/400/fast');
      $("#company-dept-code").prop("disabled", true)
      $("#name-and-title").prop("disabled", true)
      $("#telephone-no").prop("disabled", true);
      $("#date-signature").prop("disabled", true);
      $("#address").prop("disabled", true);
      $("#reporter-ref").prop("disabled", true);

    }
    else{
      //$(".main-form").fadeOut('slow/400/fast');
      $("#company-dept-code").prop("disabled", false)
      $("#name-and-title").prop("disabled", false)
      $("#telephone-no").prop("disabled", false);
      $("#date-signature").prop("disabled", false);
      $("#address").prop("disabled", false);
      $("#reporter-ref").prop("disabled", false);
    }
    
    if(radioValue =! null){
      $("#radio-error").html("");
    }

  });



});
