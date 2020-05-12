from django.forms import ModelForm
from django import forms
from globals.models import *

class technicienform(ModelForm):
    class Meta:
        model = Technicien
        fields = '__all__'
        widgets = {
                'nom' : forms.TextInput(attrs={'class':'form-control'}),
                'tel' : forms.TextInput(attrs={'class':'form-control'}),
                'email' : forms.TextInput(attrs={'class':'form-control'}),
                'login' : forms.TextInput(attrs={'class':'form-control'}),
                'password' : forms.TextInput(attrs={'class':'form-control'}),
                'type_tech' : forms.TextInput(attrs={'class':'form-control'}),
        }
"""class technicienform(forms.Form):

        nom = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
        tel = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
        email = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
        login = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
        password = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
        type_tech = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))"""


        