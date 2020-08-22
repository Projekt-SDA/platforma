from django.contrib import admin
from django.db.models import (
    CharField, DecimalField, TextField, Model, ForeignKey, DO_NOTHING,
)


class Services(Model):
    nazwa = CharField(max_length=100)
    code = CharField(max_length=13)
    cena = DecimalField(max_digits=9, decimal_places=2)
    opis = TextField(default="Proszę o dodanie opisu (opcjonalnie)", null=True)
    def __str__(self):
        return self.nazwa

class Status(Model):
    status = CharField(max_length=30)
    def __str__(self):
        return self.status


class ClientServices(Model):
    service_name = ForeignKey(Services, on_delete=DO_NOTHING)
    client_name = CharField(max_length=100)
    client_surname = CharField(max_length=100)
    client_contact_number = CharField(max_length=12)
    client_email = CharField(max_length=100)
    status = ForeignKey(Status, on_delete=DO_NOTHING)
    def __str__(self):
        return self.client_name






