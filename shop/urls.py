from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from shop import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),  # Главная страница
    path('about/', views.about, name='about'),  # Страница "О нас"
    path('products/', views.products, name='products'),  # Страница товаров
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),  # Используем слаг
    path('products/add/', views.add_product, name='add_product'),  # Используем слаг

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
