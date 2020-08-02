from django.forms import Form
from .models import Product
from django import forms

from .models import Product
from django.db.models import (
 CharField, DecimalField, TextField
)


class ProductForms(Form):
    class Meta:
        model = Product
        field=[
        "nazwa",
        "kod",
        "cena"
        ]


