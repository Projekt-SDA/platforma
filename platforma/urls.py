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
from django.urls import path, include
from django.urls import path
import sklep.views
import serwis.views
from serwis.models import Services, ClientServices, Status
from serwis.views import Service_View, ClientService_View
from sklep import views
from sklep.models import Product, Order, Cart
from sklep.views import ShopUpdateView, produkt_opis_widok, Edit_Order, Del_Order,CartUpdateView,Del_Cart
from django.contrib.auth import views as auth_views

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Cart)

admin.site.register(Services)
admin.site.register(ClientServices)
admin.site.register(Status)
#.site.register(Ongoing)
# admin.site.register(Produkty)
# admin.site.register(Dodawanie)
# admin.site.register(Person)

urlpatterns = [
    path('', views.panel),
    path('home', views.home_view, name='home'),
    path('panel/', views.panel, name='panel'),
    path('sklep', views.produkt_opis_widok),
    path('dodaj', views.formularz_dodawania_produktu),
    # path('zamowienie',views.formularz_dodawania_zamowienia, name='zamowienie'),


    path('', sklep.views.home_view),
    path('serwis', serwis.views.produkt_opis_widok, name= 'serwis'),
    path('dodaj1', serwis.views.Service_services_create_view.as_view()),
    path('waiting', serwis.views.service_product_waiting, name = 'waiting'),
    path('ongoing', serwis.views.produkt_w_realizacji),
    path('done', serwis.views.serwis_zakończony),
    path('dodaj', sklep.views.dodaj_produkt_sklep),
    path('admin/', admin.site.urls),
    path('zamowienia', views.formularz_dodawania_zamowienia, name='zamowienia'),
    path('glowna',views.home_view),
    path('koszyk', views.koszyk),
    path('test', views.test),
    path('edit/<pk>', ShopUpdateView.as_view(), name="edit"),
    path('edit_order/<pk>', Edit_Order.as_view(), name="edit_order"),
    path('Del_order/<pk>', Del_Order.as_view(), name="del_order"),
    # path('sklep/cart', views.add_cart),
    path("add_cart", views.add_cart),
    path('edit_cart/<pk>', CartUpdateView.as_view(), name="edit_cart"),
    path('del_cat/<pk>', Del_Cart.as_view(), name="del_cart"),
    # path('', include('django.contrib.auth.urls'))
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('addorder',views.add_order),
    path('del_all_cart',views.del_all_cart, name='dellallcart'),
    path('drop_db',views.drop_db, name='drop_db'),



    path('koszyk', views.koszyk),
    path('createservice', serwis.views.ServiceCreateView.as_view()),
    path('', Service_View.as_view(), name= 'index'),







]
