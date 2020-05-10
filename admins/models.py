from django.db import models

<<<<<<< HEAD
# Create your models here.

class specialite(models.Model):
    nom = models.CharField(max_length=100);
    

    def __str__(self):
        return self.nom

class technicien(models.Model):

    nomprenom = models.CharField(max_length=100);

    mail = models.CharField(max_length=100);
    tel = models.CharField(max_length=10);
    specialité = models.ForeignKey(specialite,on_delete=models.CASCADE);

=======
# Create your models here.
>>>>>>> 65ec5e689e0fa5bc7e5da48b9c88877d3451b958
