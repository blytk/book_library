from django.contrib import admin
from .models import User, Book, Note, Why, Reading, Read, Wish

# Register your models here.
admin.site.register(User)
admin.site.register(Book)
admin.site.register(Note)
admin.site.register(Why)
admin.site.register(Reading)
admin.site.register(Read)
admin.site.register(Wish)
        
