# Book Library

Web application intended to manage the books that a person is reading, has read and intends to read in the future, allowing the user to keep track, in a single place,
of all their books. 

The user can store notes for each book and download them in .txt format.

## How to run the application

The command *python3 manage.py runserver* from the application folder is all that's needed in order to start the web server with the application, assuming Django is installed on the device.

## Distinctiveness and Complexity

The project is not an ecommerce site nor a social network. It's not based on the Pizza project either. I've used a few django database models to represent the books, the reading lists and the notes (the models will be explained in more detail below).

I've added some functionality on the front-end using javascript (not included in previous projects):

- Search bar that dynamically filters the list of available books as we type
- Scrollable list that allows for an item to be selected
- Added a couple of sounds when pressing certain buttons

I've implemented a small functionality that allows the user to download .txt files, based on database queries (the user can download its notes for each book)

It's worth mentioning that, when first designing the project, I intended on adding some social features: being able to see other users lists of books or notes of books...
However, at this point, it just feels unnecessary. I don't think it would be a terrible idea to add, but would this be a live application, probably nobody would use that functionality. I feel like this is a finished product, and I would like to submit it as it is. I read often and, when taking notes for many different books, as time goes by, it can become difficult to keep track of all the notes for all the different books we have read over the years. So the target user for the app would be people like me: people that like to read books, take notes and have easy access to them, all in the same place.

### How to use the app
- There are 4 sections in the main panel (my books):
    1. All books :
        - Includes all books stored in the database (common for all users)
        - Here we can search by book or author. If the book is not in the database, the "add new book to the database" will take us to a form where we can introduce
        a new book in the database.
        - If the book we want to assign to one of our lists already exists in our database, we can search for it, click on it (it will be highlighted on the list),
        and press the appropriate button (one button for each list we want to add the book to (reading, read and wish lit))
        - Books can only be selected one by one
    2. Reading Books (clickable link):
        - Here we can see at a glance all books included in our current reading list
        - If we click on the header, we will be redirected to a page with a bit more of detail, where we can access each of the books to see its notes, remove it from the list, see other books in the database from the author or browse by genre.
    3. Read Books (clickable link):
        - Same as Reading Books, but for books already read.
    4. Wish List Books (clickable link):
        - Same as Reading Books, but for books we intend to read in the future.
    
    The navbar includes an additional page "Books with Notes", where the user can access a list, similar to the other lists, but with all the books they have added notes for.

### Models

1. *User* 
Part of Django built-in system for user authentication.

2. *Book*
Represents a book object in the database.

3. *Note*
Represents a note object, associating the text of a note with a user and a book.

4. *Reading*
Represents an element of the reading list, associating a book and an user for the reading list.

5. *Read*
Same as Reading, but for books read in the past.

6. *Wish*
Same as Reading, but for books intended to read in the future.


#### Structure of the project

*Templates* ('book_library/templates/book_library/')

- author_view.html renders a page displaying all books currently stored in the database for a particular author.
- detail_view.html renders a page displaying all the notes for a particular book, from a certain user.
- genre_view.html renders a page displaying all books currently stored in the database for a particular genre.
- layout.html contains the base layout for all html files (navigation bar).
- login.html renders the plage with a login form.
- my_books.html renders the main page, where a user can add books to the different book lists (and access them).
- new_book.html renders a page where a new book can be submitted into the database (necessary in order to add a book to one of the lists).
- register.html renders a page with a form through which an user can register to use the application.
- user_list_of_books.html renders a page where the reading lists are displayed.

*JavaScript files* ('book_library/static/book_library/')

- detail_view.js contains the JavaScript code necessary for the page rendered by the template detail_view.html
- my_books.js contains the Javascript code necessary for the page rendered by the template my_books.html
- user_list_of_books.js contains the JavaScript code necessary for the page rendered by the template user_list_of_books.html

*CSS files* ('book_library/static/book_library')

- style.css contains all the CSS code for the entire application

*Images and sounds* ('book_library/static/book_library/images'), ('book_library/static/book_library/sounds')

*.py files not existing by default on the project*

- forms.py contains the model form class used to add new books to the database ('new_book.html')
