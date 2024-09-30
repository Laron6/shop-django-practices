from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'category', 'brand', 'image']  # Поля формы

    # Кастомизация формы, добавление классов и валидации
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError('Цена должна быть больше нуля.')
        return price


class SearchForm(forms.Form):
    query = forms.CharField(label='', max_length=100, required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Название',
        'class': 'form-control',
    }))


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'autocomplete': 'text',
                'placeholder': 'Введите логин'
            }
        ),
        required=False,
        validators=[RegexValidator(r'^[^0-9а-яА-ЯёЁ]*$', "Введите логин латиницей")],
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'autocomplete': 'email',
                'placeholder': 'Введите электрону почту'
            }
        ),
        required=False
    ),
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Введите пароль'
            }
        ),
        required=False
    ),
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Повторите пароль'
            }
        ),
        required=False
    )

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if password == '':
            raise forms.ValidationError('Введите пароль', code='invalid')
        return password

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username == '':
            raise forms.ValidationError('Введите логин', code='invalid')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email == '':
            raise forms.ValidationError('Введите электронную почту', code='invalid')
        return email


class Meta(UserCreationForm.Meta):
    fields = ('username', 'email', 'password1', 'password2')
