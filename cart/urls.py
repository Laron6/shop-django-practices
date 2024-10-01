from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('detail/', views.cart_detail, name='cart_detail'),
    path('update-quantity/', views.cart_update_quantity, name='cart_update_quantity'),
    path('remove/', views.cart_remove, name='cart_remove'),
    path('clear/', views.cart_clear, name='cart_clear'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),  # Добавление товара в корзину
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
