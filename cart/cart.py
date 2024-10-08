from decimal import Decimal
from django.conf import settings
from shop.models import Product


class CartSession:
    CART_SESSION_ID = 'cart'

    # Инициализирует сессию, создает корзину, если её нет.
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(self.CART_SESSION_ID)
        if not cart:
            cart = self.session[self.CART_SESSION_ID] = {}
        self.cart = cart

    # Добавляет товар в корзину
    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    # Удаляет товар из корзины.
    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    # Проходит по корзине, возвращает товары и их количество.
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    # Возвращает общее количество товаров в корзине.
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    # Возвращает общую стоимость товаров в корзине.
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    # Очищает корзину.
    def clear(self):
        del self.session[self.CART_SESSION_ID]
        self.save()
