from django.contrib import admin
from django.db.models import (
    CharField, DecimalField, TextField, Model, ForeignKey, DateTimeField, DO_NOTHING,
)


class Services(Model):
    nazwa = CharField(max_length=100)
    code = CharField(max_length=13)
    cena = DecimalField(max_digits=9, decimal_places=2)
    opis = TextField(default="Proszę o dodanie opisu (opcjonalnie)", null=True)


class Client(Model):
    client_name = CharField(max_length=100)
    client_surname = CharField(max_length=100)
    client_contact_number = DecimalField(max_digits=9, decimal_places=2)
    client_email = CharField(max_length=100)
    opis_problemu = TextField(default="Proszę o dodanie opisu)", null=False)




class Ongoing(Model):

    client_id = ForeignKey(Client, on_delete=DO_NOTHING)
    Worker_id = 1




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
