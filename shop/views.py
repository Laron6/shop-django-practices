from django.shortcuts import render


# Главная страница
def home(request):
    return render(request, 'shop/home.html')


# Страница "О нас"
def about(request):
    return render(request, 'shop/about.html')


# Страница товаров
def products(request):
    products_list = [
        {'name': 'Смартфон', 'price': '30 000 руб.'},
        {'name': 'Наушники', 'price': '5 000 руб.'},
        {'name': 'Ноутбук', 'price': '70 000 руб.'},
        {'name': 'Смарт-часы', 'price': '12 000 руб.'},
    ]
    return render(request, 'shop/products.html', {'products': products_list})
