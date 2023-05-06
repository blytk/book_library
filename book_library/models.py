from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    pass

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=128)
    class Genre(models.IntegerChoices):
        SELF_IMPROVEMENT = 1
        BIOGRAPHY = 2
        ECONOMY = 3
        FICTION = 4
        SCIENCE = 5
        MINDSET = 6
        OTHER = 7
    genre = models.IntegerField(choices=Genre.choices)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'author'], name='one unique title per author')
        ]


    def __str__(self):
        return self.title
    

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
        }


class Note(models.Model):
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE, related_name="note_user")
    book = models.ForeignKey(Book, blank=False, null=False, on_delete=models.CASCADE, related_name="note_book")
    text = models.TextField(blank=False, null=False, max_length=512)
    # main = models.BooleanField(blank=False, null=False, default=False)


    def __str__(self):
        return f"User: {self.user}, Book: {self.book}"
    

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user,
            "book": self.book,
            "text": self.text,
            # "main": self.main,
        }

class Reading(models.Model):
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE, related_name="reading_user")
    book = models.ForeignKey(Book, blank=False, null=False, on_delete=models.CASCADE, related_name="reading_book")
    why = models.TextField(blank=True, null=True, max_length=1024)
    started_reading = models.DateField(blank=True, null=True, auto_now_add=True)
    recommend = models.BooleanField(blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'book'], name='one why per user/book reading')
        ]


    def __str__(self):
        return f"User: {self.user}, Book: {self.book}"
    

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user,
            "book": self.book
        }


class Read(models.Model):
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE, related_name="read_user")
    book = models.ForeignKey(Book, blank=False, null=False, on_delete=models.CASCADE, related_name="read_book")
    why = models.TextField(blank=True, null=True, max_length=1024)
    started_reading = models.DateField(blank=True, null=True)
    recommend = models.BooleanField(blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'book'], name='one why per user/book read')
        ]


    def __str__(self):
        return f"User: {self.user}, Book: {self.book}"
    

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user,
            "book": self.book
        }


class Wish(models.Model):
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE, related_name="wish_user")
    book = models.ForeignKey(Book, blank=False, null=False, on_delete=models.CASCADE, related_name="wish_book")
    why = models.TextField(blank=True, null=True, max_length=1024)
    recommend = models.BooleanField(blank=True, null=True)


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'book'], name='one why per user/book wish')
        ]


    def __str__(self):
        return f"User: {self.user}, Book: {self.book}"
    

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user,
            "book": self.book
        }