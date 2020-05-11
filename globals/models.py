from django.db import models

# Create your models here.

class Panne(models.Model):
    libelle_panne = models.CharField(max_length=30)

class Equipement(models.Model):
    nom_equipement=models.CharField(max_length=60)
    qte_stock=models.IntegerField()
    panne=models.ManyToManyField(Panne)

class Intervention(models.Model):
    date_intervention = models.DateField(auto_now_add=True)
    type_panne = models.ForeignKey(Panne,on_delete=models.CASCADE)
    etat = models.CharField(max_length=30)
    description = models.TextField(max_length=255)
    equipement = models.ManyToManyField(Equipement)


class Persone(models.Model):
    nom = models.CharField(max_length=30)
    email = models.EmailField()
    tel = models.CharField(max_length=8)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=32)
    #type = models.CharField()

    class Meta:
        abstract=True

class Client(Persone):
    matricule_id = models.CharField(max_length=60)

class Technicien(Persone):
    typique = models.BooleanField(default=False)
    societe = models.CharField(max_length=60,null=True)
    #intervention = models.ForeignKey(Intervention,on_delete=models.CASCADE)

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







