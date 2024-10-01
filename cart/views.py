from django.shortcuts import render, redirect
from .cart import CartSession
from shop.models import Product


def cart_detail(request):
    cart = CartSession(request)
    return render(request,
                  'cart/cart_detail.html',
                  {'cart': cart})


def cart_add(request, product_id):
    cart = CartSession(request)
    product = Product.objects.get(id=product_id)
    cart.add(product=product)
    return redirect('cart_detail')


def cart_remove(request, product_id):
    cart = CartSession(request)
    product = Product.objects.get(id=product_id)
    cart.remove(product)
    return redirect('cart_detail')
