from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
        path('validate_email/',csrf_exempt(views.EmailValidationView.as_view()),name='validate_email'),
        path('loginPage/',views.loginPage,name='loginPage'),
        path('registerPage/',views.registerPage,name='registerPage'),
        
]
