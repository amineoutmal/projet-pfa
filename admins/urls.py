from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
        path('logout/',views.logout,name='logout'),
        path('home/',views.home,name='home'),
        path('dashboard/',views.dashboard,name='dashboard'),
        path('panne/',views.panne,name='panne'),
        path('panne/<int:pk>',views.supp_panne,name='supp_panne'),
        path('form_panne/',views.forms_panne,name="ajouter_panne"),
        path('panne/<int:pk>/',views.forms_panne,name='modifier_panne'),
        path('stock/',views.stock,name='stock'),
        path('intervention/',views.intervention,name='intervention'),
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

        path('delete_interv_admin/<int:pk>',views.delete_interv_admin,name='delete_interv_admin'),

        path('track_interv/<int:pk>',views.track_interv,name='track_interv'),
        path('facturer/<int:pk>',views.facturer.as_view(),name='facturer'),
        path('profile/',views.profile,name='profileAdmin'),
        path('csvclient/',views.csv_client,name='csv-clients'),
        path('csvtechnicien/',views.csv_technicien,name='csv-technicien'),
        path('csvstock/',views.csv_stock,name='csv-stock'),
        path('csvintervention/',views.csv_intervention,name='csv-intervention'),
        
       

]
