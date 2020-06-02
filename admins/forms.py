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
                'types' : forms.Select(attrs={'class':'form-control'}),
        }

class clientform(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
                'nom' : forms.TextInput(attrs={'class':'form-control'}),
                'tel' : forms.TextInput(attrs={'class':'form-control'}),
                'email' : forms.TextInput(attrs={'class':'form-control'}),
                'login' : forms.TextInput(attrs={'class':'form-control'}),
                'password' : forms.TextInput(attrs={'class':'form-control'}),
                'matricule_id' : forms.TextInput(attrs={'class':'form-control'}),
                'adresse' : forms.TextInput(attrs={'class':'form-control'}),
        }
class stockform(ModelForm):
    class Meta:
        model = Equipement
        fields = ('nom_equipement','qte_stock')
        widgets = {
                'nom_equipement' : forms.TextInput(attrs={'class':'form-control'}),
                'qte_stock' : forms.TextInput(attrs={'class':'form-control'}),
               
        }
class panneform(ModelForm):
        class Meta:
                model = Panne
                fields ='__all__'
                widgets = widgets = {
                'libelle_panne' : forms.TextInput(attrs={'class':'form-control'}),
               
        }