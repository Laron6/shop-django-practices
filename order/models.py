from django.db import models
from shop.models import Product  # Импортируйте вашу модель продукта
from django.contrib.auth.models import User


class PaymentStatus(models.TextChoices):
    PENDING = 'PND', 'Ожидание'
    PAID = 'PD', 'Оплачено'
    FAILED = 'FLD', 'Не удалось'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)  # Поле для статуса оплаты
    payment_status = models.CharField(max_length=3, choices=PaymentStatus.choices, default=PaymentStatus.PENDING)

    def __str__(self):
        return f"Заказ #{self.id} пользователя {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} для заказа #{self.order.id}"
