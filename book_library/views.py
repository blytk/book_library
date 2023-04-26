from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.urls import reverse
from django.contrib.auth.decorators import login_required
## In case I need pagination
# from django.core.paginator import Paginator

## Import models
from .models import User, Book, Note, Reading, Read, Wish

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
    return render(request, "book_library/index.html")

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
        all_books = Book.objects.all()
        context = {"all_books": all_books}
        return render(request, "book_library/my_books.html", context)
    else:
        return HttpResponseRedirect(reverse("book_library:login"))
