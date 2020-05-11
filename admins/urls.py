from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
        path('home/',views.home,name='home'),
        path('client/',views.client,name='client'),
        path('stock/',views.stock,name='stock'),
        path('equipement/',views.equipement,name='equipement'),
        path('intervention/',views.intervention,name='intervention'),
        path('ticket/',views.ticket,name='ticket'),
        path('technicien/',views.technicien,name='technicien'),
        path('<int:pk>',views.supp_tech,name='supp_tech'),
        path('modifier/',views.modifer_tech,name='modifier_tech'),


]
