from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
        path('loginPage/',views.loginPage,name='loginPage'),
        path('registerPage/',views.registerPage,name='registerPage'),
    
]
