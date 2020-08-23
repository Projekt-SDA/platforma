from django.db import models
from django.db.models import (
 CharField, DecimalField, TextField,ForeignKey,DO_NOTHING, IntegerField, Sum
)
from django.views.generic.edit import UpdateView

class Product(models.Model):
    nazwa = CharField(max_length=100)
    code = CharField(max_length=13)
    cena = DecimalField(max_digits=9, decimal_places=2)
    ilosc = CharField(max_length=3, default='')
    opis = TextField(default="Proszę o dodanie opisu (opcjonalnie)", null=True)

    def __str__(self):
        return self.nazwa

class Order(models.Model):
    nazwa = CharField(max_length=100)
    ilosc = CharField(max_length=3)
    opis = TextField( null=True)

class Cart(models.Model):
    product = ForeignKey(Product, on_delete=DO_NOTHING)
    ilosc = IntegerField()

    @property
    def cena(self):
        return self.product.cena * self.ilosc
    @property
    def suma(self, obj):

        suma = Cart.objects.aggregate(Sum('Suma'))


        return suma


class Quantity(models.Model):
    product = ForeignKey(Product, on_delete=models.CASCADE)
    ilosc = IntegerField()

