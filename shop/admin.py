from django.contrib import admin
from .models import Category, Brand, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'brand', 'category', 'image')  # Добавляем отображение поля image
