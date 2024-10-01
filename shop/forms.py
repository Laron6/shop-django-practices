from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'category', 'brand', 'image']  # Поля формы
        labels = {
            'name': 'Название товара',
            'price': 'Стоимость',
            'description': 'Описание товара',
            'category': 'Категория',
            'brand': 'Бренд',
            'image': 'Картинка/Фото',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'min': '1', 'max': '1000000000', 'step': '1.00'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'})
        }

    # Кастомизация формы, добавление классов и валидации
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError('Цена должна быть больше нуля.')
        return price


class SearchForm(forms.Form):
    query = forms.CharField(label='', max_length=100, required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Название',
        'class': 'form-control search_query',
    }))

