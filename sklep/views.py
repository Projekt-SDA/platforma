from django.shortcuts import render
from .forms import ProductForms
from django.views.generic import FormView, ListView
from django.shortcuts import render
from .forms import ProductForms
from .models import Product

def home_view(request, *args, **kwargs):
    return render(request, "index.html", {})


def stan_sklepu(request, *args, **kwargs):
    return render(request, "sklep/stan_sklepu.html", {})


def pasek_nawigacyjny_sklep(request, *args, **kwargs):
    return render(request, "sklep/pasek_nawigacyjny_sklep.html", {})

def dodaj_produkt_sklep(request, *args, **kwargs):
    return render(request, "sklep/dodaj.html", {})




def products(request):
    return render(
        request, template_name='/sklepstan_sklepu.html',
        context={'products': Product.odjects.all()}
    )

def produkt_opis_widok(request):
    obj = Product.objects.all()
    kontekst = {
         "obiekt": obj

    }
    return render(request, "sklep/stan_sklepu.html", kontekst)

def produkt_utworz_widok(request):
    form = ProductForms(request.POST or None)

    form.save
    context = {
        "form": form
    }
    return render(request, "sklep/dodaj.html", context)



