from django.shortcuts import render
from .models import Book


def book_detail(request):
    book = Book.objects.first()  # Получаем первую книгу из базы данных
    return render(request, 'book_detail.html', {'book': book})
