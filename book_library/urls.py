from django.urls import path

from . import views

app_name ='book_library'
urlpatterns = [
    path("", views.index, name="index"),
    # User related paths
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    # END of user related paths
    path("reading/", views.reading, name="reading"),
    path("read/", views.read, name="read"),
    path("wish/", views.wish_list, name="wish"),
    path("my_books/", views.my_books, name="my_books"),
    # add books to reading, read or wish paths
    path("my_books/add_to_reading_list/<int:book_id>", views.add_to_reading_list, name="add_to_reading_list"),
    path("my_books/add_to_read_list/<int:book_id>", views.add_to_read_list, name="add_to_read_list"),
    path("my_books/add_to_wish_list/<int:book_id>", views.add_to_wish_list, name="add_to_wish_list"),
    # delete books from reading, read or wish paths
    path("my_books/delete_from_reading_list/<int:book_id>", views.remove_from_reading_list, name="add_to_reading_list"),
    path("my_books/remove_from_read_list/<int:book_id>", views.remove_from_read_list, name="add_to_read_list"),
    path("my_books/remove_from_wish_list/<int:book_id>", views.remove_from_wish_list, name="add_to_wish_list"),
    # new book form 
    path("new_book/", views.new_book, name="new_book"),
    #path("add_new_book/", views.new_book, name="add_new_book"),
]