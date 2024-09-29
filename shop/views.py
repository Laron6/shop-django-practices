from django.shortcuts import render, get_object_or_404

from shop.models import Product


# Главная страница
def home(request):
    return render(request, 'home.html')


# Страница "О нас"
def about(request):
    return render(request, 'about.html')


# Страница товаров
def products(request):
    products_list = Product.objects.all()  # Получаем все товары из базы данных
    return render(request, 'products.html', {'products': products_list})


# Страница с деталями товара

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)  # Ищем товар по слагу
    return render(request, 'product_detail.html', {'product': product})


