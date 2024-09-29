from django.forms import forms

from postmedia.models import MyModel


class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['title', 'image']

