from django.forms import ModelForm
from django import forms
from globals.models import *


class clientformprofile(ModelForm):
    class Meta:
        model = Client
        exclude = ['matricule_id']
        fields = '__all__'
        widgets = {
                'nom' : forms.TextInput(attrs={'class':'form-control'}),
                'tel' : forms.TextInput(attrs={'class':'form-control'}),
                'email' : forms.TextInput(attrs={'class':'form-control'}),
                'login' : forms.TextInput(attrs={'class':'form-control'}),
                'password' : forms.TextInput(attrs={'class':'form-control'}),
                'adresse' : forms.TextInput(attrs={'class':'form-control'}),
        }

