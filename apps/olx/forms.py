from django import forms

from .models import (
    Product,
    Order
)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'price']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'product', 'money']