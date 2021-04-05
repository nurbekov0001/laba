from django import forms
from webapp.models import Product, IntermediateTable, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'remainder', 'price')


class ProductDeleteForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Введите название задачи, чтобы удалить её')


class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False, label='Найти')


class OrderForm(forms.Form):
    class Meta:
        model = Order
        fields = ('user_name', 'phone_number', 'address')
