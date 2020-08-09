from django.db import models
from django.db.models import (
 CharField, DecimalField, TextField
)


class Product(models.Model):
    nazwa = CharField(max_length=100)
    code = CharField(max_length=13)
    cena = DecimalField(max_digits=9, decimal_places=2)
    # ilosc  = CharField(max_length=3)
    opis = TextField(default="Proszę o dodanie opisu (opcjonalnie)", null=True)


class Order(models.Model):
    nazwa = CharField(max_length=100)
    code = CharField(max_length=13)
    cena = DecimalField(max_digits=9, decimal_places=2)
    ilosc = CharField(max_length=3)
    opis = TextField(default="Zakup dla sklepu w innym przypadku zmień opis", null=True)
