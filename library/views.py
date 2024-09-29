from django.shortcuts import render
from .models import Book, Author, Publisher


def book_detail(request):
    book = Book.objects.all()  # Получаем первую книгу из базы данных
    return render(request, 'book_detail.html', {'book': book})

# from .models import Book, Author
#
# # Получаем все книги определённого автора
# def books_by_author(request, author_name):
#     # Фильтруем книги по имени автора
#     books = Book.objects.filter(author__name=author_name)
#     return render(request, 'books_by_author.html', {'books': books, 'author_name': author_name})

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
