from django import forms

from .models import Product, Order

class ProductForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
        "nazwa",
        "cena",
        # "ilosc",
        "code",
        "opis"

        ]


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
        "nazwa",
        "ilosc",
        "code",
        "opis"

        ]

