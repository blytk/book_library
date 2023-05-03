from django.forms import ModelForm
from django import forms
from .models import Book

class NewBookForm(ModelForm):
    class Meta:
        model = Book
        # fields = '__all__'
        fields = ["title", "author", "genre"]


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({'class': 'form-control'}),
        self.fields["author"].widget.attrs.update({'class': 'form-control'}),
        self.fields["genre"].widget.attrs.update({'class': 'form-control'})