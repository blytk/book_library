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
    path("my_books/", views.my_books, name="my_books"),
    # add books to reading, read or wish paths
    path("my_books/add_to_list/<int:book_id>/<str:what_list>", views.add_to_list, name="add_to_list"),
    # delete books from reading, read or wish paths 
    path("remove_from_list/<int:book_id>/<str:what_list>", views.remove_from_list, name="remove_from_list"),
    # new book form 
    path("new_book/", views.new_book, name="new_book"),
    path("detail_view/<int:user_id>/<int:book_id>", views.detail_view, name="detail_view"),
    path("user_list_of_books/<str:what_list>", views.user_list_of_books, name="user_list_of_books"),
    path("author_view/<str:author_name>", views.author_view, name="author_view"),
    path("genre_view/<int:genre>", views.genre_view, name="genre_view"),
    path("add_note/<int:book_id>", views.add_note, name="add_note"),
    path("remove_note/<int:note_id>", views.remove_note, name="remove_note"),
    # generate a .txt file (for notes on book)
    path('notes_text/<int:book_id>', views.notes_text, name="notes_text"),

]