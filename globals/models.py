from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models
 
# Create your models here.
class Panne(models.Model):
    libelle_panne = models.CharField(max_length=30)
    
    
class Equipement(models.Model):
    nom_equipement = models.CharField(max_length=60)
    qte_stock=models.IntegerField()
    prix_equipement = models.CharField(max_length=600)
    #panne=models.ManyToManyField(Panne) #a verifier
    

class Persone(models.Model):
    nom = models.CharField(max_length=30)
    email = models.EmailField()
    tel = models.CharField(max_length=8)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=32)

    class Meta:
        abstract=True

class Client(Persone):
    matricule_id = models.CharField(max_length=200)
    adresse = models.CharField(max_length=600)
class Technicien(Persone):
    TYPE = (
        ('Interne', 'Interne'),
        ('Externe', 'Externe'),
    )
    types = models.CharField(max_length=100,choices=TYPE,default=True)
    specialité = models.ForeignKey(Panne,on_delete=models.CASCADE,default=True)
    disponibilité = models.CharField(max_length=100,default=0)
    
class Fourniseur(Persone):
    materiel_demander = models.CharField(max_length=60)

class Admin(Persone):
    privelege = models.CharField(max_length=30)

class Intervention(models.Model):
    Titre_intervention = models.TextField(max_length=255)
    date_intervention = models.DateField(auto_now_add=True)
    type_panne = models.ForeignKey(Panne,on_delete=models.CASCADE)
    etat = models.CharField(max_length=30)
    description = models.TextField(max_length=255)
    image = models.ImageField(blank=True,null=True,upload_to='medial/%Y/%m/%D')
    equipements = models.ManyToManyField(Equipement)
    clients = models.ForeignKey(Client,on_delete=models.CASCADE,default=True)
    latitude = models.FloatField(default=True)
    longtude = models.FloatField(default=True)
    fulladresses = models.TextField(max_length=1000,default=True)
    date_fin = models.TextField(max_length=255,default=False)
    durée_mission = models.TextField(max_length=255,default=False)

class Affectation(models.Model):

    tech=models.ForeignKey(Technicien,on_delete=models.CASCADE)
    Inter=models.ForeignKey(Intervention,on_delete=models.CASCADE)
    date_affectation = models.DateField(auto_now_add=True)
    date_resolution = models.DateField(null=True)

class Commande(models.Model):

    fourniseur=models.ForeignKey(Fourniseur,on_delete=models.CASCADE)
    equipement=models.ForeignKey(Equipement,on_delete=models.CASCADE)
    prix = models.FloatField()
    QTE = models.IntegerField()
 
class Facturation(models.Model):

    clients = models.ForeignKey(Client,on_delete=models.CASCADE,default=True)
    interventions = models.ForeignKey(Intervention,on_delete=models.CASCADE,default=True)
    etat = models.CharField(max_length=30,default=0)
    date_facturation = models.DateField(auto_now_add=True)

class Priorité(models.Model):
    libelle_priorité = models.TextField(max_length=255,default=False)
    delai = models.TextField(max_length=255,default=False)

class Detail_equipement(models.Model):

    equipements=models.ForeignKey(Equipement,on_delete=models.CASCADE,default=True)
    interventions=models.ForeignKey(Intervention,on_delete=models.CASCADE)
    QTE = models.IntegerField(default=True)