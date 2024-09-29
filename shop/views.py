from django.shortcuts import render, get_object_or_404, redirect
from django.db import models
from shop.forms import ProductForm, SearchForm
from shop.models import Product


# Главная страница
def home(request):
    return render(request, 'home.html')


# Страница "О нас"
def about(request):
    return render(request, 'about.html')


# Страница товаров
# def products(request):
#     products_list = Product.objects.all()  # Получаем все товары из базы данных
#     return render(request, 'products.html', {'products': products_list})


# Страница с деталями товара

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)  # Ищем товар по слагу
    return render(request, 'product_detail.html', {'product': product})


# Добавление нового товара
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')  # Перенаправляем на страницу со списком товаров
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


# Редактирование товара
def edit_product(request, slug):
    product = Product.objects.get(slug=slug)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form, 'product': product})


def products(request):
    form = SearchForm(request.GET or None)  # Инициализация формы поиска
    products_list = Product.objects.all()

    # Проверяем, был ли запрос
    if form.is_valid():
        query = form.cleaned_data.get('query')
        if query:
            # Фильтруем товары по названию или описанию
            products_list = products_list.filter(
                models.Q(name__icontains=query) | models.Q(description__icontains=query)
            )

    return render(request, 'products.html', {'products': products_list, 'form': form})
