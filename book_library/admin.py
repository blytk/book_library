from django.contrib import admin
from .models import User, Book, Note, Why

# Register your models here.
admin.site.register(User)
admin.site.register(Book)
admin.site.register(Note)
admin.site.register(Why)
        
