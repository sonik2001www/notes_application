$(document).ready(function(){
    $('.archive-button').on('click', function(){
        var noteId = $(this).data('note-id');
        $.ajax({
            url: '/note/' + noteId + '/archive/',
            type: 'POST',
            dataType: 'json',
            data: {
                csrfmiddlewaretoken: csrfToken
            },
            success: function(response){
                if (response.success) {
                    location.reload();
                }
            }
        });
    });

    $('.unarchive-button').on('click', function(){
        var noteId = $(this).data('note-id');
        $.ajax({
            url: '/note/' + noteId + '/unarchive/',
            type: 'POST',
            dataType: 'json',
            data: {
                csrfmiddlewaretoken: csrfToken
            },
            success: function(response){
                if (response.success) {
                    location.reload();
                }
            }
        });
    });
});
