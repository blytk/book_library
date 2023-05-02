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
    path("my_books/add_to_list/<int:book_id>/<str:what_list>", views.add_to_list, name="add_to_list"),
    # delete books from reading, read or wish paths 
    # I need to think about this, where to remove from. Probably a good idea to make a "see all my reading books, read books, wish books, and allow to remove from there"
    # path("my_books/remove_from_reading_list/<int:book_id>", views.remove_from_list, name="remove_from_list"),
    # new book form 
    path("new_book/", views.new_book, name="new_book"),
    path("detail_view/<int:user_id>/<int:book_id>", views.detail_view, name="detail_view"),
    path("user_list_of_books/<str:what_list>", views.user_list_of_books, name="user_list_of_books"),
    path("author_view/<str:author_name>", views.author_view, name="author_view"),
    path("genre_view/<int:genre>", views.genre_view, name="genre_view"),


]