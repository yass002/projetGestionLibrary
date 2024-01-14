import datetime
from django.db import models
from datetime import timedelta,date
from django.utils import timezone

# Create your models here.
class Adherent(models.Model):
    nomAdh = models.CharField(max_length=30)
    prenomAdh = models.CharField(max_length=30)
    adresseAdh = models.CharField(max_length=30,default='Iteam University')
    dateNaissanceAdh = models.DateField(null=True)
    emailAdh = models.EmailField(unique=True , null=True, blank=True)
    nbrEmpruntAdh = models.IntegerField(null=True,blank=True,default=0)
    imageSrc = models.ImageField(upload_to='images/', null=True)
  
    
class Auteur(models.Model):
    nomAuteur = models.CharField(max_length=30)
    prenomAuteur = models.CharField(max_length=30)

class Livre(models.Model):
    titreLivre = models.CharField(max_length=30)
    nbrePageLivre = models.IntegerField()
    codeAuteur = models.ForeignKey(Auteur, on_delete=models.CASCADE , blank=True,null=True)
    nbrEmpruntLivre = models.IntegerField(default=0)
    adhEmprunteur = models.ManyToManyField('Adherent' , through='Emprunt')
    imageSrc = models.ImageField(upload_to='images/', null=True)
    nbExemplaire = models.IntegerField(null=True)

    

class Emprunt(models.Model):
    adherent = models.ForeignKey(Adherent, on_delete=models.CASCADE)
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)    
    date_emprunt = models.DateField(default=datetime.date.today)
    date_retour_prevu = models.DateField(null=True)
    date_retour_effectif = models.DateField(null=True, blank=True)
    est_en_retard = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        # Check if date_effectif is not set already
     
        if not self.date_retour_prevu:
            now = date.today()
            # Set date_effectif to current date plus 15 days
            self.date_retour_prevu = now + timedelta(days=15)

        super().save(*args, **kwargs)

class Statistiques(models.Model):
    totalLivres= models.IntegerField()
    livresEmpruntes = models.IntegerField()
      