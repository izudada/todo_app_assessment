function csrfHeaders() {
    return {
        'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value
    };
}

$(document).ready(function () {
    // click event on the todo checkbpx
    $('.my-check').click(function (input) {
        var inputID = input.target.id;

        $.ajax({
            url: `${inputID}/completed/`,
            type: 'post',
            data: {
                'todo': inputID,
            },
            headers: csrfHeaders(),
            success: function (response) {
            },
            error: function(error) {
                console.log(error)
            }
        });
    });
});