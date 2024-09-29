from django.db import models
from django.utils.text import slugify


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
    image = models.ImageField(upload_to='products/', blank=True, null=True)  # Поле для загрузки изображения
    slug = models.SlugField(unique=True, max_length=100)  # Новое поле для слага

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  # Автоматически генерируем слаг на основе имени
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


