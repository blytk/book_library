document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#add-to-reading-button').addEventListener('click', function() {
        book_id_to_send = clickedLi;
        // I need to post the url "my_books/add_to_reading_list/<int:book_id>" that will trigger the view add_to_reading_list(request, book_id)
        fetch(`add_to_reading_list/${book_id_to_send}`, {
            method: 'POST'
        })
        document.querySelector('#alert').innerHTML = "Book successfully added to reading list"
        document.querySelector('#alert').style.display = "block"

        
        // add to reading button function
        // I am adding a book to a list, so I need to grab the book object, from the list, somehow
        // HOOW????? When I click the item, I can grab book id, and operate with the id
        
    });
    document.querySelector('#add-to-read-button').addEventListener('click', function() {
        //add to read button function
    });
    document.querySelector('#add-to-wish-button').addEventListener('click', function() {
        //add to wish button function
    });

    // I want to make the li items "selectable", visually and to grab it's id to pass onto the list
    // I don't know how to make only one item selectable simultaneously. Maybe I make it work as a list? Better experience actually
    // I am going to get started with just one item selected, as the view function expects a single book id
    // I might review later to see if I can make it work with a list and it's better overall
    let items = document.querySelectorAll('#allbooks-div li')
    selected = 0
    items.forEach(li => {
        li.addEventListener('click', () => {
            if (selected === 0) {
                li.classList.toggle('selected');
                selected = 1
                clickedLi = li.id
            } else if (li.id === clickedLi) {
                li.classList.toggle('selected');
                selected = 0
            }
        }) 
    });
})