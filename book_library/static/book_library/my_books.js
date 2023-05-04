document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#add-to-reading-button').addEventListener('click', function() {
        book_id_to_send = clickedLi;
        // I need to post the url "my_books/add_to_reading_list/<int:book_id>" that will trigger the view add_to_reading_list(request, book_id)
        fetch(`add_to_list/${book_id_to_send}/reading_list`, {
            method: 'POST',
        })
        message = document.querySelector('#alert')
        message.innerHTML = "Book successfully added to reading list"
        message.className = ""
        message.classList.add("alert")
        message.classList.add("alert-success")
        message.style.display = "block"

        setTimeout(function() {
            location.reload()},
            2000)

        
        // add to reading button function
        // I am adding a book to a list, so I need to grab the book object, from the list, somehow
        // HOOW????? When I click the item, I can grab book id, and operate with the id
        
    });
    document.querySelector('#add-to-read-button').addEventListener('click', function() {
        //add to read button function
        book_id_to_send = clickedLi;
        fetch(`add_to_list/${book_id_to_send}/read_list`, {
            method: 'POST',
        })

        message = document.querySelector('#alert')
        message.innerHTML = "Book successfully added to read list"
        message.className = ""
        message.classList.add("alert")
        message.classList.add("alert-primary")
        message.style.display = "block"
        setTimeout(function() {
            location.reload()},
            2000)
    });

    document.querySelector('#add-to-wish-button').addEventListener('click', function() {
        //add to wish button function
        book_id_to_send = clickedLi;
        fetch(`add_to_list/${book_id_to_send}/wish_list`, {
            method: 'POST',
        })

        message = document.querySelector('#alert')
        message.innerHTML = "Book successfully added to wish list"
        message.className = ""
        message.classList.add("alert")
        message.classList.add("alert-info")
        message.style.display = "block"
        setTimeout(function() {
        location.reload()},
        2000)
    });

    // I want to make the li items "selectable", visually and to grab it's id to pass onto the list
    // I don't know how to make only one item selectable simultaneously. Maybe I make it work as a list? Better experience actually
    // I am going to get started with just one item selected, as the view function expects a single book id
    // I might review later to see if I can make it work with a list and it's better overall
    let all_books_li = document.querySelectorAll('#allbooks-div li')
    selected = 0
    all_books_li.forEach(li => {
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
   document.querySelector('#search').addEventListener('keyup', filter);
})


// Search bar filter functionality
function filter() {
    // Capture the value of the search bar (what is currently entered in the search box)
    searchValue = document.querySelector('#search').value;
    searchValue = searchValue.toLowerCase();
    
    // Capture all the li from the menu
    all_books = document.querySelectorAll('#menu li');
    all_books.forEach(li => {
        title = li.innerHTML;
        title = title.toLowerCase();
        // Check for each book, if the search value is included in the title of the book
        if (title.includes(searchValue)) {
            li.classList.add('visible');
            li.classList.remove('hidden');
        } else {
            li.classList.add('hidden');
            li.classList.remove('visible');
        }
    })
};


function play() {
    var audio = new Audio('/static/book_library/sounds/page-flip-4.mp3')
    audio.play();
};

document.querySelector('#add-to-reading-button').addEventListener('click', play);
document.querySelector('#add-to-read-button').addEventListener('click', play);
document.querySelector('#add-to-wish-button').addEventListener('click', play);
