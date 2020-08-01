from django.forms import Form
from .models import Product_serv
from django.db.models import (
 CharField, DecimalField, TextField
)


class ProductForms(Form):
    nazwa = CharField(max_length=100)
    code = CharField(max_length=13)
    cena = DecimalField(max_digits=9, decimal_places=2)
    opis = TextField(default="Proszę o dodanie opisu (opcjonalnie)", null=True)



