from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from shop.models import Product
from order.models import Order, OrderItem
from cart.cart import CartSession


class OrderProcessTest(TestCase):
    def setUp(self):
        # Создание пользователя
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Создание товара для тестирования
        self.product = Product.objects.create(
            name='Test Product',
            price=100.00,
            description='Test Description',
            brand=None,  # Предполагается, что бренд можно пропустить или создать отдельно
            image=None  # Можно оставить пустым для теста
        )

    def test_order_process(self):
        # 1. Пользователь регистрируется
        self.assertEqual(User.objects.count(), 1)  # Проверяем, что пользователь зарегистрирован

        # 2. Пользователь входит в систему
        self.client.login(username='testuser', password='testpassword')

        # 3. Добавляем товар в корзину
        response = self.client.post(reverse('cart_add', args=[self.product.id]))  # добавляем товар в корзину
        self.assertEqual(response.status_code, 302)  # Проверяем, что происходит перенаправление

        # 4. Проверяем, что товар добавлен в корзину
        cart = CartSession(self.client)
        self.assertEqual(len(cart), 1)  # Товар должен быть в корзине
        self.assertEqual(cart.get_total_price(), 100.00)  # Проверяем итоговую сумму

        # 5. Оформляем заказ
        response = self.client.post(reverse('checkout'), {
            'full_name': 'Test User',
            'address': 'Test Address',
            'phone': '1234567890',
            'email': 'testuser@example.com'
        })
        self.assertEqual(response.status_code, 302)  # Проверяем перенаправление на страницу успеха

        # 6. Проверяем, что заказ был создан
        order = Order.objects.first()  # Получаем первый заказ
        self.assertIsNotNone(order)  # Проверяем, что заказ существует
        self.assertEqual(order.user, self.user)  # Проверяем, что заказ принадлежит правильному пользователю
        self.assertEqual(order.items.count(), 1)  # Проверяем, что в заказе один товар
        self.assertEqual(order.items.first().product, self.product)  # Проверяем, что товар соответствует

        # 7. Проверяем итоговую сумму заказа
        self.assertEqual(order.items.first().quantity, 1)  # Проверяем количество товара
        self.assertEqual(order.items.first().product.price, 100.00)  # Проверяем цену товара

        total_price = sum(item.product.price * item.quantity for item in order.items.all())
        self.assertEqual(total_price, 100.00)  # Проверяем, что итоговая сумма заказа соответствует
