from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from shop.models import Product, Category, Brand
from order.models import Order, OrderItem, PaymentStatus
from cart.cart import CartSession


class OrderProcessTest(TestCase):
    def setUp(self):
        # Создаем категорию и бренд для тестирования, так как они обязательны
        self.category = Category.objects.create(name='Test Category')
        self.brand = Brand.objects.create(name='Test Brand')

        # Создаем пользователя
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Создаем товар с обязательными полями (image можно не заполнять)
        self.product = Product.objects.create(
            name='Test Product',
            price=100.00,
            description='Test Description',
            category=self.category,
            brand=self.brand,
            image_url='http://example.com/test_product.jpg',  # Можно использовать image_url
            slug='test-product'  # Обязательно нужно указать slug
        )

    def test_order_process(self):
        # 1. Пользователь регистрируется
        self.assertEqual(User.objects.count(), 1)  # Проверяем, что пользователь зарегистрирован

        # 2. Пользователь входит в систему
        self.client.login(username='testuser', password='testpassword')

        # 3. Добавляем товар в корзину
        response = self.client.post(reverse('cart_add', args=[self.product.id]))  # добавляем товар в корзину
        self.assertEqual(response.status_code, 302)  # Проверяем, что происходит перенаправление

        # Проверяем, что товар в корзине
        cart = CartSession(self.client)
        self.assertEqual(len(cart), 1)  # Товар должен быть в корзине

        # 4. Оформляем заказ, передавая данные формы
        response = self.client.post(reverse('checkout'), {
            'full_name': 'Test User',
            'address': '123 Test St.',
            'phone': '1234567890',
            'email': 'testuser@example.com',
            'payment_status': PaymentStatus.PENDING,  # Добавляем скрытый статус платежа
        })
        self.assertEqual(response.status_code, 302)  # Проверяем перенаправление на страницу успеха

        # 5. Проверяем, что заказ был создан
        order = Order.objects.first()  # Получаем первый заказ
        self.assertIsNotNone(order)  # Проверяем, что заказ существует
        self.assertEqual(order.user, self.user)  # Проверяем, что заказ принадлежит правильному пользователю
        self.assertEqual(order.items.count(), 1)  # Проверяем, что в заказе один товар
        self.assertEqual(order.items.first().product, self.product)  # Проверяем, что товар соответствует

        # 6. Проверяем итоговую сумму заказа
        total_price = sum(item.product.price * item.quantity for item in order.items.all())
        self.assertEqual(total_price, 100.00)  # Проверяем, что итоговая сумма заказа соответствует


