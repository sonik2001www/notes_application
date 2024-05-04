document.addEventListener('DOMContentLoaded', function() {
  var colorInput = document.getElementById('id_color');
  var jscolorInputs = document.getElementsByClassName('jscolor');

  for (var i = 0; i < jscolorInputs.length; i++) {
    jscolorInputs[i].addEventListener('input', function() {
      colorInput.value = this.value;
    });
  }
});
