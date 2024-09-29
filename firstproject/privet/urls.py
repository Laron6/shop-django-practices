from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_privet, name='get_privet'),  # маршрут для вывода сообщения
]
