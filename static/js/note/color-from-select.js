document.addEventListener('DOMContentLoaded', function () {
    var categorySelect = document.getElementById('id_category');

    var categoryOptions = Array.from(categorySelect.options).slice(1);

    var lastCategoryOption = categoryOptions.reduce(function(prev, current) {
        return (parseInt(prev.value) > parseInt(current.value)) ? prev : current;
    });

    lastCategoryOption.selected = true;

    var colorSpan = document.getElementById('color');

    function updateTextColor() {
        var selectedOption = categorySelect.options[categorySelect.selectedIndex];
        var optionText = selectedOption.textContent.trim();
        var background = optionText.split(' ')[1];
        colorSpan.style.background = background;
    }

    updateTextColor();

    categorySelect.addEventListener('change', updateTextColor);
});

