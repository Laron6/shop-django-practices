from django.shortcuts import render

from shop.models import Product


# Главная страница
def home(request):
    return render(request, 'shop/home.html')


# Страница "О нас"
def about(request):
    return render(request, 'shop/about.html')


# Страница товаров
def products(request):
    products_list = Product.objects.all()  # Получаем все товары из базы данных
    return render(request, 'shop/products.html', {'products': products_list})
