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

        // I get the li element I want to add, I clone it to not modify the original, append it into the appropriate list
        selected_book = document.querySelector('.selected')        
        var selectedBookClone = selected_book.cloneNode(true)
        selectedBookClone.textContent = selected_book.querySelector('.book-title-span').textContent
        selectedBookClone.classList.remove("selected")

        // I need to check that the element is not already on the list, this doesn't affect the database but it looks bad (adds same title more than once if clicked more)
        var checkLiNodeList = document.querySelectorAll('#readingbooksmenu li')
        
        already_exists = false;
        checkLiNodeList.forEach(node => {
            if (node.textContent === selectedBookClone.textContent) {
                already_exists = true;
            }
        })

        if (already_exists === false) {
            document.querySelector('#readingbooksmenu').append(selectedBookClone)
        }
        
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
        

        // I get the li element I want to add, I clone it to not modify the original, append it into the appropriate list
        selected_book = document.querySelector('.selected')        
        var selectedBookClone = selected_book.cloneNode(true)
        selectedBookClone.textContent = selected_book.querySelector('.book-title-span').textContent
        selectedBookClone.classList.remove("selected")

        // I need to check that the element is not already on the list, this doesn't affect the database but it looks bad (adds same title more than once if clicked more)
        var checkLiNodeList = document.querySelectorAll('#readbooksmenu li')
        
        already_exists = false;
        checkLiNodeList.forEach(node => {
            if (node.textContent === selectedBookClone.textContent) {
                already_exists = true;
            }
        })

        if (already_exists === false) {
            document.querySelector('#readbooksmenu').append(selectedBookClone)
        }
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
        
        // I get the li element I want to add, I clone it to not modify the original, append it into the appropriate list
        selected_book = document.querySelector('.selected')        
        var selectedBookClone = selected_book.cloneNode(true)
        selectedBookClone.textContent = selected_book.querySelector('.book-title-span').textContent
        selectedBookClone.classList.remove("selected")

        // I need to check that the element is not already on the list, this doesn't affect the database but it looks bad (adds same title more than once if clicked more)
        var checkLiNodeList = document.querySelectorAll('#wishlistmenu li')
        
        already_exists = false;
        checkLiNodeList.forEach(node => {
            if (node.textContent === selectedBookClone.textContent) {
                already_exists = true;
            }
        })

        if (already_exists === false) {
            document.querySelector('#wishlistmenu').append(selectedBookClone)
        }
    });

    // I want to make the li items "selectable", visually and to grab it's id to pass onto the list
    // I don't know how to make only one item selectable simultaneously. Maybe I make it work as a list? Better experience actually
    // I am going to get started with just one item selected, as the view function expects a single book id
    // I might review later to see if I can make it work with a list and it's better overall
    /*
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
    */
   let all_books_li = document.querySelectorAll('#allbooks-div li')
    all_books_li.forEach(li => {
        li.addEventListener('click', () => {
            all_books_li.forEach(li => {
                li.classList.remove('selected');
            })
            li.classList.add('selected');
            clickedLi = li.id
        })
    })

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

    // Blink effect on add-to buttons (3 buttons total)
    let allAddToButtons = document.querySelectorAll('.add-to-button')
    allAddToButtons.forEach(addToButton => {
        addToButton.addEventListener('mouseover', () => { 
            addToButton.classList.add('blink');
        })
        addToButton.addEventListener('mouseout', () => { 
            addToButton.classList.remove('blink');
        })  
    });