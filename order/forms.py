from django import forms

from order.models import PaymentStatus, Order


class OrderForm(forms.ModelForm):
    full_name = forms.CharField(
        label='ФИО',
        max_length=100,
        widget=forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Фамилию Имя Отчество'
            })
    )
    address = forms.CharField(label='Адрес', max_length=255)
    phone = forms.CharField(label='Телефон', max_length=15)
    email = forms.EmailField(label='Электронная почта')
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
            'full_name': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Фамилию Имя Отчество'
            }),
            'user_phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите контактный номер телефона',
            }),
            'user_email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите электронную почту',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите адрес',
                'rows': 3
            }),
        }
        error_messages = {
            'user_phone': {
                'max_length': 'О себе не должно превышать 11 символов',
            },
        }
