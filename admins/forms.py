from django import forms
from globals.models import *


class technicienform(forms.Form):

        nom = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
        tel = forms.CharField(max_length=100)
        email = forms.CharField(max_length=100)
        login = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
        password = forms.CharField(max_length=100)
        type = forms.CharField(max_length=100)


        