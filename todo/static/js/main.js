function csrfHeaders() {
    // A function to get and return csrf token
    return {
        'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value
    };
}

let completedTodo = () => {
    $.ajax({
        url: `search/`,
        type: 'post',
        data: {
            'todo': 'completed',
        },
        headers: csrfHeaders(),
        success: function (response) {
            // Remove the ul
            $( ".item" ).remove();

            // create array for respose data for completed todos
            var listItem = [];

            // loop todos to make a list item
            for(let i=0; i < response.data.length; i++) {
                listItem.push(`
                    <li>
                        <a href="{% url 'detail' ${response.data[i].id} %}">${response.data[i].title}</a>
                        <input type="checkbox" id="${response.data[i].id}" class="my-check" checked>
                    </li>
                `);
            } 

            // Append items to new ul
            $("h1").after(`<ul class="item"> ${listItem} </ul>`)
        },
        error: function(error) {
            console.log(error)
        }
    });
}

$(document).ready(function () {
    // click event on the todo checkbox
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


    $('.search').click(function (anchor) {
        // events for search filters/buttons
        anchor.preventDefault();
        const ANCHOR = anchor.target.innerText;

        switch(ANCHOR) {
            case "Completed":
              completedTodo();
              break;
            case "Pending":
              // code block
              break;
            default:
              window.location.reload();
        }
    });
});