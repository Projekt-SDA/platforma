from django.db import models
from django.db.models import (
 CharField, DecimalField, TextField, Model
)


class Product(Model):
    nazwa = CharField(max_length=100)
    code = CharField(max_length=13)
    cena = DecimalField(max_digits=9, decimal_places=2)
    opis = TextField(default="Proszę o dodanie opisu (opcjonalnie)", null=True)
#
#
# class Produkty(Model):
#     nazwa = CharField(max_length=100)
#     code = CharField(max_length=13)
#     cena = DecimalField(max_digits=9, decimal_places=2)
#     opis = TextField(default="Proszę o dodanie opisu (opcjonalnie)", null=True)
#
#
# class Dodawanie(Model):
#     nazwa = CharField(max_length=100)
#
#
# class Person(Model):
#     imie = CharField(max_length=120)
#     nazwisko = CharField(max_length=120)
#
# class Persons(Model):
#         imie = CharField(max_length=120)
#         nazwisko = CharField(max_length=120)