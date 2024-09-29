from django import forms
from .models import Book, Author, Publisher

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'year', 'author', 'publisher']  # Поля, которые мы хотим использовать в форме
