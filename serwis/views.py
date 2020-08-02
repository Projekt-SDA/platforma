

from django.views.generic import FormView, ListView
from django.shortcuts import render

from .models import Services

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
