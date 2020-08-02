from django.shortcuts import render
from .forms import ProductForms, OrderForm
from .models import Product, Order

def home_view(request, *args, **kwargs):
    return render(request, "index.html", {})


def stan_sklepu(request, *args, **kwargs):
    return render(request, "sklep/stan_sklepu.html", {})


def pasek_nawigacyjny_sklep(request, *args, **kwargs):
    return render(request, "sklep/pasek_nawigacyjny_sklep.html", {})

def dodaj_produkt_sklep(request, *args, **kwargs):
    return render(request, "sklep/dodaj.html", {})

def zamowienia(request, *args, **kwargs):
    return render(request, "sklep/zamowienia.html", {})

def koszyk(request, *args, **kwargs):
    return render(request, "sklep/koszyk.html", {})

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



def formularz_dodawania_produktu(request):
 form = ProductForms(request.POST or None)
 if form.is_valid():
      form.save(commit = True)
      form = ProductForms
 context = {
      "form": form
  }

 return render(request,"sklep/dodaj.html", context)



def zamowienia_opis_widok(request):
    obj = Order.objects.all()
    kontekst = {
        "obiekt": obj

    }
    return render(request, "sklep/zamowienia.html", kontekst)


def formularz_dodawania_zamowienia(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save(commit=True)
        form = OrderForm
    context = {
        "form": form
    }

    return render(request, "sklep/zamowienia.html", context)
