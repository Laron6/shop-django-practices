from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Регистрация
    path('register/', views.register, name='register'),
    # Вход в систему
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    # Выход из системы
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





