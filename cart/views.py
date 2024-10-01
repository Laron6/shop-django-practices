from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

from order.forms import OrderForm
from .cart import CartSession
from shop.models import Product


def cart_detail(request):
    cart = CartSession(request)
    form = OrderForm()
    return render(request,
                  'cart/cart_detail.html',
                  {'cart': cart, 'form': form})


def cart_add(request, product_id):
    cart = CartSession(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect('cart_detail')  # Перенаправляем на страницу корзины


def cart_update_quantity(request):
    cart = CartSession(request)
    product_id = request.POST.get('product_id')
    change = int(request.POST.get('change'))

    product = Product.objects.get(id=product_id)
    quantity = cart.cart[str(product.id)]['quantity'] + change

    if quantity > 0:
        cart.add(product=product, quantity=quantity, update_quantity=True)
    else:
        cart.remove(product)

    response = {
        'quantity': quantity,
        'item_total_price': cart.cart[str(product.id)]['quantity'] * float(cart.cart[str(product.id)]['price']),
        'total_price': cart.get_total_price(),
    }

    return JsonResponse(response)


def cart_remove(request):
    cart = CartSession(request)
    product_id = request.POST.get('product_id')
    product = Product.objects.get(id=product_id)
    cart.remove(product)

    response = {
        'total_price': cart.get_total_price(),
    }

    return JsonResponse(response)


def cart_clear(request):
    cart = CartSession(request)
    cart.clear()

    response = {
        'total_price': cart.get_total_price(),
    }

    return JsonResponse(response)
