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
from serwis.models import Services, ClientServices
from serwis.views import Service_View, ClientService_View
from sklep import views
from sklep.models import Product, Order


admin.site.register(Product)
admin.site.register(Order)

admin.site.register(Services)
admin.site.register(ClientServices)
#.site.register(Ongoing)
# admin.site.register(Produkty)
# admin.site.register(Dodawanie)
# admin.site.register(Person)

urlpatterns = [

    path('', views.home_view),

    path('sklep', views.produkt_opis_widok),
    path('dodaj', views.formularz_dodawania_produktu),

    path('', sklep.views.home_view),
    # path('dodaj/', views.Dodaj_produkt_sklep),
    path('sklep', sklep.views.produkt_opis_widok),
    path('serwis', serwis.views.produkt_opis_widok),
    path('dodaj1', serwis.views.Service_services_create_view.as_view()),
    path('waiting', ClientService_View.as_view(), name = 'waiting'),
    path('ongoing', serwis.views.produkt_w_realizacji),
    path('done', serwis.views.serwis_zakończony),
    path('dodaj', sklep.views.dodaj_produkt_sklep),
    path('admin/', admin.site.urls),
    path('zamowienia', views.zamowienia_opis_widok),
    path('glowna',views.home_view),
    path('koszyk', views.koszyk)

    path('', Service_View.as_view(), name= 'index'),







]
