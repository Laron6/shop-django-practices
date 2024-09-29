from django.contrib import admin
from .models import Book, Author, Publisher


# Настройка отображения модели Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'author')  # Поля, которые будут отображаться в списке
    list_filter = ('author', 'year')  # Добавляем фильтр по автору и году
    search_fields = ('title', 'author__name')  # Добавляем поиск по названию книги и имени автора
    filter_horizontal = ('publisher',)  # Для удобного выбора связей с издателями


# Настройка отображения модели Author
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth', 'gender')
    search_fields = ('name',)  # Добавляем поиск по имени автора


# Настройка отображения модели Publisher
@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)  # Добавляем поиск по названию издательства

