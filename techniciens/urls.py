from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('acceuil-technicien/',views.home,name='acceuil-technicien'),
    #path('creer-intervention/',views.creer_intervention,name='creer-intervention'),

]
