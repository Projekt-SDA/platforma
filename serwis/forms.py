from django.forms import (CharField, ModelChoiceField, Form, ModelForm
)

from serwis.models import ClientServices, Services



class ServiceForm(Form):
    nazwa_usługi = ModelChoiceField(queryset=Services.objects)
    Imię = CharField(max_length=100)
    Nazwisko = CharField(max_length=100)
    Numer_Kontaktowy = CharField(max_length=12)
    E_mail = CharField(max_length=100)

class ServiceForm(ModelForm):

    class Meta:
        model = ClientServices
        fields = '__all__'












