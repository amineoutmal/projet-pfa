from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
        path('acceuil/',views.home,name='acceuil'),
        path('creer-intervention/',views.creer_intervention,name='creer-intervention'),
        path('mes-intervention/',views.mes_intervention,name='mes-intervention'),
        path('validate_interv/<int:pk>',views.validate_interv,name='validate_interv'),
        path('delete_interv/<int:pk>',views.delete_interv,name='delete_interv'),

]