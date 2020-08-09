from django.forms import (CharField, ModelChoiceField, Form, ModelForm, DecimalField
)

from serwis.models import ClientServices, Services
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row,Submit


class ServiceForm(Form):
    nazwa_usługi = ModelChoiceField(queryset=Services.objects)
    Imię = CharField(max_length=100)
    Nazwisko = CharField(max_length=100)
    Numer_Kontaktowy = CharField(max_length=12)
    E_mail = CharField(max_length=100)

class ServiceForm(ModelForm):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(self, *args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         'service_name',
    #         Row(Column('client_name'), Column('client_surname'), Column('client_contact_number'),Column('client_email')),
    #         Submit('Submit', 'Submit')
    #
    #     )
    class Meta:
        model = ClientServices
        fields = '__all__'

class ServicessForm(Form):
    nazwa = CharField(max_length=100)
    code = CharField(max_length=13)
    cena = DecimalField(max_digits=9, decimal_places=2)
    opis = CharField(initial="Proszę o dodanie opisu (opcjonalnie)")

class ServicessForm(ModelForm):
    class Meta:
        model = Services
        fields = '__all__'












