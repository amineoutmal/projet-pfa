from django.db import models
 
# Create your models here.
class Panne(models.Model):
    libelle_panne = models.CharField(max_length=30)
    
    
class Equipement(models.Model):
    nom_equipement=models.CharField(max_length=60)
    qte_stock=models.IntegerField()
    panne=models.ManyToManyField(Panne)

class Intervention(models.Model):
    Titre_intervention = models.TextField(max_length=255)
    date_intervention = models.DateField(auto_now_add=True)
    type_panne = models.ForeignKey(Panne,on_delete=models.CASCADE)
    etat = models.CharField(max_length=30)
    description = models.TextField(max_length=255)
    image = models.ImageField(blank=True,null=True,upload_to='medial/%Y/%m/%D')
    equipement = models.ManyToManyField(Equipement)

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

class Fourniseur(Persone):
    materiel_demander = models.CharField(max_length=60)

class Admin(Persone):
    privelege = models.CharField(max_length=30)

class Affectation(models.Model):
    tech=models.ForeignKey(Technicien,on_delete=models.CASCADE)
    Inter=models.ForeignKey(Intervention,on_delete=models.CASCADE)
    date_affectation = models.DateField(auto_now_add=True)
    date_resolution = models.DateField()

class Commande(models.Model):
    fourniseur=models.ForeignKey(Fourniseur,on_delete=models.CASCADE)
    equipement=models.ForeignKey(Equipement,on_delete=models.CASCADE)
    prix = models.FloatField()
    QTE = models.IntegerField()
 

