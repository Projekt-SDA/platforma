from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ProductForms, OrderForm, CartForm
from .models import Product, Order
from logging import getLogger
from django.db.models import Q
import sqlite3
from django.http import HttpResponse
from django.shortcuts import redirect

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView,DeleteView

# from viewer.forms import ProductForms
# from viewer.models impor Product
from .models import Cart
LOGGER = getLogger()
@login_required
def home_view(request):
    return render(request, "index.html", {})

@login_required
def panel(request):
    return render (request,"index.html")

def test(request, *args, **kwargs):
    return render(request, "sklep/test.html", {})


def stan_sklepu(request, *args, **kwargs):
    return render(request, "sklep/stan_sklepu.html", {})


def pasek_nawigacyjny_sklep(request, *args, **kwargs):
    return render(request, "sklep/pasek_nawigacyjny_sklep.html", {})

def dodaj_produkt_sklep(request, *args, **kwargs):
    return render(request, "sklep/dodaj.html", {})

def zamowienia(request, *args, **kwargs):
    return render(request, "sklep/zamowienia.html", {})

def koszyk(request, *args, **kwargs):

    obj = Cart.objects.all()

    kontext = {
        "obiekt": obj

    }

    return render(request, "sklep/koszyk.html", {"obj": obj})

def products(request):
    return render(
        request, template_name='/sklepstan_sklepu.html',
        context={'products': Product.odjects.all()}
    )

def produkt_opis_widok(request):

    query = request.GET.get("q", None)
    obj = Product.objects.all()
    if query is not None:
        obj = obj.filter(
            Q(nazwa__icontains=query)|
            Q(code__icontains=query))




    kontekst = {
         "obiekt": obj

    }

    return render(request, "sklep/stan_sklepu.html", kontekst)



def formularz_dodawania_produktu(request):
    form = ProductForms(request.POST or None)
    if form.is_valid():
        form.save(commit = True)
        form = ProductForms()
    context = {
      "form": form
    }

    return render(request,"sklep/dodaj.html", context)



def zamowienia_opis_widok(request):
    obj = Order.objects.all()
    kontext = {
        "obiekt": obj

    }
    return render(request, "sklep/zamowienia.html", kontext)




def formularz_dodawania_zamowienia(request):
    form = OrderForm(request.POST or None)
    obj = Order.objects.all()
    if form.is_valid():
        form.save(commit = True)
        form = OrderForm
    context = {
        "form": form,
        "obiekt": obj

    }

    return render(request, "sklep/zamowienia.html", context)




class ShopUpdateView(UpdateView):
    model = Product
    template_name = "form.html"

    fields = [
        "nazwa",
        "ilosc",
        "cena",
        "code"
    ]
    success_url ="/sklep"


# def add_cart(request):
#
#     obj = Product.objects.all()
#     kontext = {
#         "obiekt": obj
#
#     }
#     return render(request, "sklep/cart.html", kontext)

class Edit_Order(UpdateView):
    model = Order
    template_name = "form.html"

    fields = [
        "nazwa",
        "ilosc",
        "opis"

    ]
    success_url ="/zamowienia"


class Del_Order(DeleteView):
    model = Order
    template_name = "sklep/delete_form.html"

    fields = [
        "nazwa",
        "ilosc",
        "opis"

    ]
    success_url ="/zamowienia"


def koszyk_dodanie_produktu(request):
    obj = Cart.objects.all()
    kontext = {
        "obiekt": obj

    }
    return render(request, "sklep/stan_sklepu.html", kontext)


def add_cart(request):
    form = CartForm(request.POST or None)
    obj = Cart.objects.all()
    if form.is_valid():
     form.save(commit = True)
     form = CartForm
    context = {
        "form": form,
        "obj":obj
    }


    return render(request,"sklep/add_cart.html", context)



class CartUpdateView(UpdateView):
    model = Product
    template_name = "form.html"

    fields = [
        "nazwa",
        "ilosc",
        "cena",
        "code"
    ]
    success_url ="/koszyk"



class Del_Cart(DeleteView):
    model = Cart
    template_name = "sklep/delete_form.html"

    fields = [
        "nazwa",
        "ilosc",
        "opis"

    ]
    success_url ="/koszyk"

@login_required
def profile(request):
    return render(request, 'users/profile.html')

def add_order(request):
    form = OrderForm(request.POST or None)

    if form.is_valid():
        form.save(commit = True)
        form = OrderForm
    context = {
        "form": form,

    }


    return render(request,"sklep/addorder.html", context)



class Del_Order_All(DeleteView):
    model = Order
    template_name = "sklep/delete_form.html"

    fields = [
        "nazwa",
        "ilosc",
        "opis"

    ]
    success_url ="/zamowienia"
def del_all_cart(request):


    Cart.objects.all().delete()

    context= {

    }

    return render(request, 'sklep/cart.html', context)


def drop_db(request):
    conn = sqlite3.connect('db.sqlite3')

    cursor = conn.cursor()


    cursor.execute("DELETE FROM sklep_cart")
    print("Table usunięta:) ")


    conn.commit()


    conn.close()
    return redirect('/koszyk')

def my_custom_sql(request):
    from django.db import connection, transaction
    cursor = connection.cursor()

    # cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s")
    # transaction.commit_unless_managed()

    cursor.execute("select * from sqlite_master where type='table'")
     # print("Table dropped... ")
    return HttpResponse(cursor.fetchone())