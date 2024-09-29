from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Главная страница
    path('about/', views.about, name='about'),  # Страница "О нас"
    path('products/', views.products, name='products'),  # Страница товаров
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
