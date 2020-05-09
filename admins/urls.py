from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
        path('home/',views.home,name='home'),
        path('client/',views.home,name='client'),
        path('stock/',views.home,name='stock'),
        path('equipement/',views.home,name='equipement'),
        path('intervention/',views.home,name='intervention'),
        path('ticket/',views.home,name='ticket'),
        path('technicien/',views.home,name='technicien'),


]
