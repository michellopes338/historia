$(document).ready(function() {
    $('a.transition').click(function() {
        const link = $(this).attr('link');
        $('.interface').load(link);
    });
})