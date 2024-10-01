from .cart import CartSession


def cart_count(request):
    cart = CartSession(request)
    return {'cart_items_count': len(cart)}
