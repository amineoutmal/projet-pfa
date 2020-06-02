from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('acceuil/',views.home,name='acceuil'),
    #path('creer-intervention/',views.creer_intervention,name='creer-intervention'),

]
