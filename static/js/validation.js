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

      document.getElementById("company-dept-code").required = false;
      document.getElementById("name-and-title").required = false;
      $("#telephone-no").removeAttr('required');
      $("#date-signature").removeAttr('required');
      $("#address").removeAttr('required');
      $("#reporter-ref").removeAttr('required');

    }
    else{
      //$(".main-form").fadeOut('slow/400/fast');
      $("#company-dept-code").prop("disabled", false)
      $("#name-and-title").prop("disabled", false)
      $("#telephone-no").prop("disabled", false);
      $("#date-signature").prop("disabled", false);
      $("#address").prop("disabled", false);
      $("#reporter-ref").prop("disabled", false);

      $("#company-dept-code").prop("required", false)
      $("#name-and-title").prop("required", false)
      $("#telephone-no").prop("required", false);
      $("#date-signature").prop("required", false);
      $("#address").prop("required", false);
      $("#reporter-ref").prop("required", false);
    }

    if(radioValue =! null){
      $("#radio-error").html("");
    }

  });



});
