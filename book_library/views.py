# Json stuff
import json
from django.http import JsonResponse
#
from django.forms import ModelForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
## In case I need pagination
# from django.core.paginator import Paginator

## Import models
from .models import User, Book, Note, Reading, Read, Wish

# Import forms
from .forms import NewBookForm

# Create your views here.


# User related views (login, logout, register)
#####################################################################################################################################################################
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication is successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("book_library:index"))
        else:
            return render(request, "book_library/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "book_library/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("book_library:index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "book_library/register.html", {
                "message": "Passwords must match."
            })
        
        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "book_library/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("book_library:index"))
    else:
        return render(request, "book_library/register.html")
    

# End of user related views
#####################################################################################################################################################################


def index(request):
    # Redirect to my_books while I figure out what to do for the main page (maybe it will stay as my_books)
    return HttpResponseRedirect(reverse("book_library:my_books"))
    # return render(request, "book_library/index.html")

# Should I pass the user as an argument? I am thinking maybe not, as the user will always be request.user
# However, in order to see lists from other people, it may be necessary. I will review later.

def reading(request):
    # User logged in?
    if request.user.is_authenticated:
        # I need to get the books for the logged in user
        reading_objects = Reading.objects.filter(user=request.user)
        # I think when I filter I don't need to try / except, as if the filter cannot find any results, it will return the empty queryset
        # (and the .get will raise an error if it doesn't find the object)
        context = {"reading_objects": reading_objects}
        return render(request, "book_library/reading.html", context)
    else:
        return HttpResponseRedirect(reverse("book_library:login"))


def read(request):
    if request.user.is_authenticated:
        read_objects = Read.objects.filter(user=request.user)
        context = {"read_objects": read_objects}
        return render(request, "book_library/read.html", context)
    else:
        return HttpResponseRedirect(reverse("book_library:login"))


def wish_list(request):
    if request.user.is_authenticated:
        wish_objects = Wish.objects.filter(user=request.user)
        context = {"wish_objects": wish_objects}
        return render(request, "book_library/wish.html", context)
    else:
        return HttpResponseRedirect(reverse("book_library:login"))


def my_books(request):
    if request.user.is_authenticated:
        all_books = Book.objects.all().order_by("title")
        reading_books = Reading.objects.filter(user=request.user)
        read_books = Read.objects.filter(user=request.user)
        wish_books = Wish.objects.filter(user=request.user)

        context = {"all_books": all_books, "reading_books": reading_books, "read_books": read_books, "wish_books": wish_books}
        return render(request, "book_library/my_books.html", context)
    else:
        return HttpResponseRedirect(reverse("book_library:login"))


def user_list_of_books(request, what_list):
    print(what_list)
    if what_list == "all_books":
        user_list_of_books = Book.objects.all().order_by("title")
    elif what_list == "reading_books":
        user_list_of_books = Reading.objects.filter(user=request.user)
    elif what_list == "read_books":
        user_list_of_books = Read.objects.filter(user=request.user)
    elif what_list == "wish_books":
        user_list_of_books = Wish.objects.filter(user=request.user)
    
    context = {"user_list_of_books": user_list_of_books, "what_list": what_list}
    return render(request, "book_library/user_list_of_books.html", context)


def author_view(request, author_name):
    books_by_author = Book.objects.filter(author=author_name).order_by("title")
    context = {"books_by_author": books_by_author, "author_name": author_name}
    return render(request, "book_library/author_view.html", context)


def genre_view(request, genre):
    books_by_genre = Book.objects.filter(genre=genre).order_by("title")
    erst = books_by_genre[0]
    context = {"books_by_genre": books_by_genre, "erst": erst}
    return render(request, "book_library/genre_view.html", context)



#### ADD NEW BOOK

def new_book(request):
        # Create new book element
        form = NewBookForm()
        context = {'form': form}
        if request.method == "POST":
            form = NewBookForm(request.POST)
            # Capture title and author entered by user
            title = request.POST.get("title")
            author = request.POST.get("author")
            # Check if title and author already exist, as there can only be one unique pair title/author and it will raise an error
            if Book.objects.filter(title=title).exists() and Book.objects.filter(author=author).exists():
                    
                    message = "A book from the same author with the same title already exists in the database"
                    context = {'form': form, 'message': message}
                    return render(request, "book_library/new_book.html", context)

            if form.is_valid(): 
                print("3")
                
                form.save()
                form = NewBookForm()
                message = "Book added successfully"
                context = {'form': form, 'message': message}
                return render(request, "book_library/new_book.html", context)
                #return HttpResponseRedirect(reverse("book_library:new_book"))
        else:
            return render(request, "book_library/new_book.html", context)

    

# I am going to make three different functions, one for each list, after they are done, I will unify them in a single function, using list (to what list we add) as
# a third argument

###### ADD BOOKS TO LISTS VIEWS ######### (reading, read, wish) (this is going to be used through JS in the app)
@csrf_exempt
def add_to_list(request, book_id, what_list):
    if request.method == "POST":
    # I have to somehow capture the book from the list        
        try:
            book = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return JsonResponse(status=400)
    # I have to create a new object Reading.object and add the relevant data to the fields
    # Check to what list we want to add a book (reading, read or wish)
        if what_list == "reading_list":
            new_entry = Reading()
            
        elif what_list == "read_list":
            new_entry = Read()
            
        elif what_list == "wish_list":
            new_entry = Wish()

        new_entry.user = request.user
        new_entry.book = book    
            
        
        try:
            new_entry.save()
        except:
            return JsonResponse({"message": "Error adding book to the list"})
        
        return JsonResponse({"message": "Book added successfully."})
    else:
        return JsonResponse({"message": "Only POST requests allowed"})


###### REMOVE BOOKS FROM LISTS VIEWS ######### (reading, read, wish) (this is going to be used through JS in the app)
@csrf_exempt
def remove_from_list(request, book_id, what_list):
    if request.method == "POST":
        # Capture book from the list
        try:
            book = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return JsonResponse({"message": "Book doesn't exist"})
        # I have the book I need to delete, what list?

        if what_list == "reading_books":
            try:                
                entry_to_capture = Reading.objects.get(user=request.user, book=book)
                entry_to_capture.delete()
                print("hello")
            except Reading.DoesNotExist:
                return JsonResponse({"message": "Error removing book to the list"})
        elif what_list == "read_books":
            try:
                entry_to_capture = Read.objects.get(user=request.user, book=book)
                entry_to_capture.delete()
            except Read.DoesNotExist:
                return JsonResponse({"message": "Error removing book to the list"})
        elif what_list == "wish_books":
            try:
                entry_to_capture = Wish.objects.get(user=request.user, book=book)
                entry_to_capture.delete()
            except Wish.DoesNotExist:
                return JsonResponse({"message": "Error removing book to the list"})
        return JsonResponse({"message": "Book removed successfully"})
    else:
        return JsonResponse({"message": "Only POST requests allowed"})

        

### DETAIL VIEW 
def detail_view(request, user_id, book_id):
    # We get the user we what (from url) and the book we want (from url too)
    current_user = User.objects.get(id=user_id)
    current_book = Book.objects.get(id=book_id)
    # Get all the notes the one user has for the one book
    notes = Note.objects.filter(book=current_book, user=current_user)
    context = {'current_user': current_user, 'current_book': current_book, 'notes': notes}
    return render(request, "book_library/detail_view.html", context)


