from django.shortcuts import render, redirect

from .forms import BookForm
from .models import Book, Author, Publisher


def book_detail(request):
    book = Book.objects.first()  # Получаем первую книгу из базы данных
    return render(request, 'book_detail.html', {'book': book})


# Функция для отображения всех книг одного автора
def books_by_author(request, author_id):
    author = Author.objects.get(id=author_id)  # Получаем автора по его ID
    books = Book.objects.filter(author=author)  # Фильтруем книги по автору
    return render(request, 'books_by_author.html', {'author': author, 'books': books})


# Функция для отображения всех книг, связанных с одним издателем
def books_by_publisher(request, publisher_id):
    publisher = Publisher.objects.get(id=publisher_id)  # Получаем издателя по его ID
    books = publisher.book_set.all()  # Получаем все книги, связанные с этим издателем
    return render(request, 'books_by_publisher.html', {'publisher': publisher, 'books': books})


def book_list(request):
    books = Book.objects.all()  # Получаем все книги из базы
    return render(request, 'book_list.html', {'books': books})


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():  # Проверяем, валидна ли форма
            form.save()  # Сохраняем книгу в базе данных
            return redirect('book_detail')  # Перенаправляем на список книг
    else:
        form = BookForm()  # Если не POST, создаем пустую форму
    return render(request, 'add_book.html', {'form': form})
