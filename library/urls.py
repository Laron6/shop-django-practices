from django.urls import path
from . import views

urlpatterns = [
    path('first/', views.book_detail, name='book_detail'),  # маршрут для отображения книги
    # Маршрут для книг автора
    path('author/<int:author_id>/', views.books_by_author, name='books_by_author'),

    # Маршрут для книг издателя
    path('publisher/<int:publisher_id>/', views.books_by_publisher, name='books_by_publisher'),

    path('add-book/', views.add_book, name='add_book'),
    path('books/', views.book_list, name='book_list'),  # Новый маршрут для списка книг
]
