from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('logout_technicien',views.logout_technicien,name='logout_technicien'),
    path('acceuil-technicien/',views.home,name='acceuil-technicien'),
    path('mes_interventions/',views.mes_interventions,name='mes_interventions'),
    path('track_interv_technicien/<int:pk>',views.track_interv_technicien,name='track_interv_technicien'),
    path('terminer/<int:pk>',views.terminer,name='terminer'),
    path('profile/',views.profile,name='profile'),


    

]
