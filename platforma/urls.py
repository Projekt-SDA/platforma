"""platforma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import sklep.views
import serwis.views
from sklep.models import Product
from serwis.models import Product_serv

admin.site.register(Product)
admin.site.register(Product_serv)
# admin.site.register(Produkty)
# admin.site.register(Dodawanie)
# admin.site.register(Person)

urlpatterns = [

    path('', sklep.views.home_view),
    # path('dodaj/', views.Dodaj_produkt_sklep),
    path('sklep', sklep.views.produkt_opis_widok),
    path('serwis', serwis.views.produkt_opis_widok),
    path('dodaj1', serwis.views.dodaj_produkt_serwis),
    path('ongoing', serwis.views.produkt_oczekujący),
    path('done', serwis.views.serwis_zakończony),
    path('dodaj', sklep.views.dodaj_produkt_sklep),
    path('admin/', admin.site.urls),




]
