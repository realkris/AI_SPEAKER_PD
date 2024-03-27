$(document).ready(function() {
    var wrapper = $("#button-wrapper");
    $(".submit").click(function(e) {
        e.preventDefault(); // Prevent the default anchor tag behavior
        if (!wrapper.hasClass("checked")) {
            wrapper.addClass("checked");
            setTimeout(function() {
                wrapper.removeClass("checked");
                $("#videoForm").submit();
            }, 4000); 
        }
    });
});


