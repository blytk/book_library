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
    path("my_books/", views.my_books, name="my_books")
]