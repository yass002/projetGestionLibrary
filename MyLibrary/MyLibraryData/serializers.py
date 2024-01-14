from rest_framework import serializers
from .models import *

class AdherentSerialize(serializers.ModelSerializer):


    class Meta:
        model = Adherent
        fields = ['id','nomAdh','prenomAdh','emailAdh','adresseAdh','dateNaissanceAdh','nbrEmpruntAdh','imageSrc']
        
    def imageSrcSetter(self, value):
        self._imageSrc = "http://localhost:8000/media/" + str(value)
        return self._imageSrc

class AutorSerialize(serializers.ModelSerializer):
    class Meta:
        model=Auteur
        fields= "__all__"  
    
   
     
class LivreSerialize(serializers.ModelSerializer):
    codeAuteur=serializers.PrimaryKeyRelatedField(queryset=Auteur.objects.all())
    nbrEmpruntLivre=serializers.SerializerMethodField()
    class Meta:
        model= Livre
        fields = ["id", "titreLivre", "nbrePageLivre", "codeAuteur","nbrEmpruntLivre","adhEmprunteur","imageSrc","nbExemplaire"]
 
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['codeAuteur'] = AutorSerialize(instance.codeAuteur).data
        return representation

    def get_nbrEmpruntLivre(self, obj):
        return obj.nbrEmpruntLivre 
    





class EmpruntSerialize(serializers.ModelSerializer):
    adherent = serializers.PrimaryKeyRelatedField(queryset=Adherent.objects.all())
    livre = serializers.PrimaryKeyRelatedField(queryset=Livre.objects.all())
    class Meta:
        model=Emprunt
        fields="__all__"
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['adherent'] = AdherentSerialize(instance.adherent).data
        representation['livre'] = LivreSerialize(instance.livre).data
        return representation