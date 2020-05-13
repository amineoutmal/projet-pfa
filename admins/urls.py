from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
        path('home/',views.home,name='home'),
        path('stock/',views.stock,name='stock'),
        path('intervention/',views.intervention,name='intervention'),
        path('ticket/',views.ticket,name='ticket'),
        path('technicien/',views.technicien,name='technicien'),
        path('form_technicien/',views.forms_technicien,name="ajouter_technicien"),
        path('technicien/<int:pk>/',views.forms_technicien,name='modifier_technicien'),
        path('technicien/<int:pk>',views.supp_tech,name='supp_tech'),

        path('form_stock/',views.forms_equipement,name="ajouter_equipement"),
        path('stock/<int:pk>/',views.forms_equipement,name='modifier_equipement'),
        path('stock/<int:pk>',views.supp_equip,name='supp_equip'),

        path('client/<int:pk>/',views.forms_client,name='modifier_client'),
        path('client/<int:pk>',views.supp_clt,name='supp_clt'),
        path('client/',views.client,name='client'),
        path('form_client/',views.forms_client,name='ajouter_client'),
       

]
