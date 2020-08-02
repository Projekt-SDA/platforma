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
from sklep import views
from sklep.models import Product, Order


admin.site.register(Product)
admin.site.register(Order)


urlpatterns = [

    path('', views.home_view),

    path('sklep', views.produkt_opis_widok),
    path('dodaj', views.formularz_dodawania_produktu),

    path('admin/', admin.site.urls),
    path('zamowienia', views.zamowienia_opis_widok),
    path('glowna',views.home_view),
    path('koszyk', views.koszyk)




]
