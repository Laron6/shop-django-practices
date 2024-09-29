from django.db import migrations


def add_initial_data(apps, schema_editor):
    Category = apps.get_model('shop', 'Category')
    Brand = apps.get_model('shop', 'Brand')
    Product = apps.get_model('shop', 'Product')

    # Создание категорий
    smartphones = Category.objects.create(name='Смартфоны', description='Мобильные устройства и аксессуары')
    laptops = Category.objects.create(name='Ноутбуки', description='Ноутбуки и аксессуары')

    # Создание брендов
    apple = Brand.objects.create(name='Apple')
    samsung = Brand.objects.create(name='Samsung')

    # Создание товаров
    Product.objects.create(
        name='iPhone 13',
        price=85000,
        description='Смартфон с процессором A15 Bionic и потрясающей камерой.',
        category=smartphones,
        brand=apple,
        image_url='https://example.com/iphone13.jpg',
        image='products/iphone.jpg'
    )

    Product.objects.create(
        name='Samsung Galaxy S21',
        price=75000,
        description='Флагманский смартфон с экраном 120Hz и мощной камерой.',
        category=smartphones,
        brand=samsung,
        image_url='https://example.com/galaxys21.jpg',
        image='products/galaxyS21.jpg'
    )

    Product.objects.create(
        name='MacBook Pro 14',
        price=200000,
        description='Ноутбук с процессором M1 и невероятной производительностью.',
        category=laptops,
        brand=apple,
        image_url='https://example.com/macbookpro.jpg',
        image='products/macbook.jpg'
    )

    Product.objects.create(
        name='Samsung Galaxy Book',
        price=120000,
        description='Ультратонкий ноутбук с AMOLED-экраном и длительным временем работы.',
        category=laptops,
        brand=samsung,
        image_url='https://example.com/galaxybook.jpg',
        image='products/galaxyBook.jpg'
    )


class Migration(migrations.Migration):
    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_initial_data),
    ]
