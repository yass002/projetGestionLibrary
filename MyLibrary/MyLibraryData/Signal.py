from django.db.models.signals import post_save,pre_save,post_delete
from django.dispatch import receiver
from .models import Emprunt, Livre

@receiver(post_save, sender=Emprunt)
def update_nb_emprunts_livre(sender, instance, **kwargs):
    livre = instance.livre
    livre.nbrEmpruntLivre = Emprunt.objects.filter(livre=livre).count()   
    livre.save()

@receiver(post_save , sender=Emprunt)
def update_nb_exemplaire_livre(sender,instance,**kwargs):

    if  not instance.date_retour_effectif:
        print("Borrow Book Signal Called")
        livre = instance.livre
        livre.nbExemplaire = livre.nbExemplaire - 1
        livre.save()


@receiver(post_save , sender=Emprunt)
def update_nb_exemplaire_livre(sender,instance,**kwargs):
    if  instance.date_retour_effectif:
        livre = instance.livre
        livre.nbExemplaire = livre.nbExemplaire + 1
        livre.save()