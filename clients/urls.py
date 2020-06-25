from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
        path('acceuil/',views.home,name='acceuilclient'),
        path('creer-intervention/',views.creer_intervention,name='creer-intervention'),
        path('mes-intervention/',views.mes_intervention,name='mes-intervention'),
        path('mes-facture/',views.mes_facture,name='mes-facture'),
        path('validate_interv/<int:pk>',views.validate_interv,name='validate_interv'),
        path('delete_interv/<int:pk>',views.delete_interv,name='delete_interv'),
        path('logout_client',views.logout_client,name='logout_client'),
        path('valider_intervention/<int:pk>',views.valider_intervention,name='valider_intervention'),
        path('profile/',views.profile,name='profileClient'),
        path('csv_client/',views.csv_client,name='csv-interv'),
]