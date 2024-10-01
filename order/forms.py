from django import forms

from order.models import PaymentStatus, Order


class OrderForm(forms.ModelForm):
    # Добавляем статус оплаты (можно сделать скрытым полем, если не нужно показывать пользователю)
    payment_status = forms.ChoiceField(choices=PaymentStatus.choices, widget=forms.HiddenInput(),
                                       initial=PaymentStatus.PENDING)

    class Meta:
        model = Order
        fields = ['full_name', 'user_phone', 'user_email', 'address']
        labels = {
            'full_name': 'ФИО',
            'user_phone': 'Телефон',
            'user_email': 'Электронная Почта',
            'address': 'Адрес',
        }
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия Имя Отчество',
                'required': True
            }),
            'user_phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона',
                'required': True
            }),
            'user_email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Электронная почта',
                'required': True
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите адрес',
                'rows': 3,
                'required': True
            }),
        }
        error_messages = {
            'user_phone': {
                'max_length': 'О себе не должно превышать 11 символов',
            },
        }
