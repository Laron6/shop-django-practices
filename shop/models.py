from django.db import models


# Модель Категория
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# Модель Бренд
class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Модель Товар
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image_url = models.URLField(max_length=200, blank=True)  # URL изображения товара

    def __str__(self):
        return self.name
