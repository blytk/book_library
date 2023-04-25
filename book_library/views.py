from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.urls import reverse
from django.contrib.auth.decorators import login_required
## In case I need pagination
# from django.core.paginator import Paginator

## Import models
from .models import User, Book, Note, Why, Reading, Read, Wish

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
            return HttpResponseRedirect(reverse("index"))
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


def reading(request):
    # I need to get the books for the logged in user
    return render(request, "book_library/index.html")