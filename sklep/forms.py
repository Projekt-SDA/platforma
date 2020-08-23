from django import forms

from .models import Product, Order, Cart

class ProductForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "nazwa",
            "cena",
            "ilosc",
            "code",
            "opis"

        ]


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "nazwa",
            "ilosc",
            "opis"

        ]

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = [
            "product",
            "ilosc"
        ]
class QuantityForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = [
            "product",
            "ilosc"
        ]
