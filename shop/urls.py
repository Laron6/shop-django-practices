from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from shop import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Главная страница
    path('about/', views.about, name='about'),  # Страница "О нас"
    path('products/', views.products, name='products'),  # Страница товаров
    # path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),  # Используем слаг

    # Регистрация
    path('register/', views.register, name='register'),
    # Вход в систему
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # Выход из системы
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
