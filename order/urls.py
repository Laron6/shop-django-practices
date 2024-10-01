from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('order-success/', views.order_success, name='order_success'),  # URL для успешного заказа
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
