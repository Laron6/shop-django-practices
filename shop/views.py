from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.db import models
from shop.forms import ProductForm, SearchForm, RegisterForm
from shop.models import Product
from django.contrib.auth.decorators import login_required


# Главная страница
def home(request):
    return render(request, 'home.html')


# Страница "О нас"
def about(request):
    return render(request, 'about.html')


# Страница с деталями товара
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)  # Ищем товар по слагу
    return render(request, 'product_detail.html', {'product': product})


@login_required
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


@login_required
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


# def register(request: HttpRequest):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.save()
#             return redirect('home')
#     else:
#         form = RegisterForm()
#     return render(request, 'register.html', context={
#         'title': 'Регистрация',
#         'form': form,
#     })

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт {username} был успешно создан!')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
