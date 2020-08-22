from django.views.generic import  ListView, CreateView, UpdateView
from django.shortcuts import render
from logging import getLogger
from django.urls import reverse_lazy
from serwis.models import ClientServices
from serwis.models import Services
from serwis.forms import ServiceForm,ServicessForm

LOGGER = getLogger()



class Service_View(ListView):
    template_name = 'stan_serwis.html'
    model = Services

class Service_services_create_view(CreateView):
    template_name = 'serwis/dodaj1.html'
    form_class = ServiceForm
    success_url = reverse_lazy('waiting')

class ServiceServicesUpdateView(UpdateView):
    template_name = 'serwis/dodaj1.html'
    model = ClientServices
    form_class = ServiceForm
    success_url = reverse_lazy('waiting')

class ClientService_View(ListView):
    template_name = 'waiting.html'
    model = ClientServices

class ServiceCreateView(CreateView):
    template_name = 'serwis/createservice.html'
    form_class = ServicessForm
    success_url = reverse_lazy('serwis')





def home_view(request, *args, **kwargs):
    return render(request, "index.html", {})


def stan_serwis(request, *args, **kwargs):
    return render(request, "serwis/stan_serwis.html", {})


def nawigacja_serwis(request, *args, **kwargs):
    return render(request, "serwis/nawigacja_serwis.html", {})

def dodaj_produkt_serwis(request, *args, **kwargs):
    return render(request, "serwis/dodaj1.html", {})

def produkt_oczekujący(request, *args, **kwargs):
    return render(request, 'serwis/waiting.html', {})

def produkt_w_realizacji(request, *args, **kwargs):
    return render(request, 'serwis/ongoing.html', {})

def serwis_zakończony(request, *args, **kwargs):
    return render(request, 'serwis/done.html', {})


def services(request):
    return render(
        request, template_name='stan_serwis.html',
        context={'product':Services.odjects.all()}
    )


def produkt_opis_widok(request):
    obj = Services.objects.all()
    kontekst = {
         'obiekt': obj

    }
    return render(request, "serwis/stan_serwis.html", kontekst)

def service_product_waiting(request):
    client_services = ClientServices.objects.all()
    kontekst = {
        'services' : client_services
    }
    return  render(request,'serwis/waiting.html',kontekst)


