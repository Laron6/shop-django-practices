from django.http import HttpRequest
from django.shortcuts import render, redirect

from cart.cart import CartSession
from order.forms import OrderForm
from order.models import Order, OrderItem


# Create your views here.
def checkout(request: HttpRequest):
    cart = CartSession(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                user=request.user,
                paid=False,  # По умолчанию, при создании заказа, он не оплачен
                payment_status=form.cleaned_data['payment_status'],
                full_name=form.cleaned_data['full_name'],
                user_phone=form.cleaned_data['user_phone'],
                user_email=form.cleaned_data['user_email'],
                address=form.cleaned_data['address'],
            )
            for item in cart:
                print(f"Добавление {item['quantity']} x {item['product'].name} в заказ")
                OrderItem.objects.create(order=order, product=item['product'], quantity=item['quantity'])
            # form.save()
            print(f"Создан заказ с ID: {order.id}")
            print(f"Итоговая сумма: ", cart.get_total_price())
            cart.clear()  # Очищаем корзину после оформления заказа
            return redirect('order_success')  # Перенаправление на страницу успеха
    else:
        form = OrderForm()
    return render(request, 'order/checkout.html', {'form': form, 'cart': cart})


def order_success(request):
    return render(request, 'order/success.html')  # Шаблон для успешного оформления заказа

