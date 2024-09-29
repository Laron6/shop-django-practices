from django.contrib import admin
from .models import Author, Publisher, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth', 'gender')


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'author')
    filter_horizontal = ('publisher',)  # Для удобного выбора в связи многие-ко-многим
