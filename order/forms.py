from django import forms

from order.models import PaymentStatus


class OrderForm(forms.Form):
    full_name = forms.CharField(label='ФИО', max_length=100)
    address = forms.CharField(label='Адрес', max_length=255)
    phone = forms.CharField(label='Телефон', max_length=15)
    email = forms.EmailField(label='Электронная почта')
    # Добавляем статус оплаты (можно сделать скрытым полем, если не нужно показывать пользователю)
    payment_status = forms.ChoiceField(choices=PaymentStatus.choices, widget=forms.HiddenInput(),
                                       initial=PaymentStatus.PENDING)
