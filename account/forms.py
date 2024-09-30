from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django import forms

from account.models import Profile


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


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(
            attrs={
                'autocomplete': 'text',
                'placeholder': 'Логин'
            }
        ),
        required=False
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                'placeholder': 'Пароль'
            }
        ),
        required=False
    ),

    error_messages = {
        "invalid_login": (
            "Введите логин и пароль правильно"
        ),
    }

    def clean_password(self):
        password = self.cleaned_data.get('password1')
        if password == '':
            raise forms.ValidationError('Введите пароль', code='invalid')
        return password

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username == '':
            raise forms.ValidationError('Введите логин', code='invalid')
        if not User.objects.filter(username=username):
            raise forms.ValidationError('Такого пользователя не существует', code='invalid')
        return username


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date']
        labels = {
            'bio': 'О себе',
            'location': 'Местоположение',
            'birth_date': 'Дата рождения',
        }
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите о себе...',
                'rows': 4,
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше местоположение',
            }),
            'birth_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
        }
        error_messages = {
            'bio': {
                'max_length': 'О себе не должно превышать 500 символов',
            },
            'birth_date': {
                'invalid': 'Введите правильную дату рождения',
            },
        }

