from django import forms
from webapp.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'remainder', 'price')


class ProductDeleteForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Введите название задачи, чтобы удалить её')
