from django.core.management.base import BaseCommand
from shop.models import Product
from django.utils.text import slugify


class Command(BaseCommand):
    help = 'Обновляет слаги для всех товаров'

    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        for product in products:
            if not product.slug:
                product.slug = slugify(product.name)
                product.save()
                self.stdout.write(self.style.SUCCESS(f'Слаг обновлен для {product.name}'))
