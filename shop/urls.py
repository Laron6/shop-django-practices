from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Главная страница
    path('about/', views.about, name='about'),  # Страница "О нас"
    path('products/', views.products, name='products'),  # Страница товаров
]
