from django.forms import ModelForm
from django import forms
from globals.models import *


class technicienformprofile(ModelForm):
    class Meta:
        model = Technicien
        fields = ('nom','tel','email','login','password')
        widgets = {
                'nom' : forms.TextInput(attrs={'class':'form-control'}),
                'tel' : forms.TextInput(attrs={'class':'form-control'}),
                'email' : forms.TextInput(attrs={'class':'form-control'}),
                'login' : forms.TextInput(attrs={'class':'form-control'}),
                'password' : forms.TextInput(attrs={'class':'form-control'}),
        }
