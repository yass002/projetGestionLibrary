from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AdherentSerialize,LivreSerialize,AutorSerialize,EmpruntSerialize
from rest_framework import status
from .models import Adherent, Livre , Auteur , Emprunt
from rest_framework import viewsets
import datetime
from datetime import date
from django.db import transaction
from django.db.models import F


#Ajout des adherents
@api_view(['POST'])
def ajouterAdherent(request):
        serializer = AdherentSerialize(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
#Get All adherent
@api_view(['GET'])
def afficherToutesAdherent(request):
      try:
            adherents = Adherent.objects.order_by('nomAdh').all()
            serializer = AdherentSerialize(adherents, many=True)
            return Response(serializer.data)
      except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST) 
#Get adherent by id       
@api_view(['GET'])
def afficherAdherent(request, id):
      try:
            adherent = Adherent.objects.get(id=id)
            serializer = AdherentSerialize(adherent)
            return Response(serializer.data)
      except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def supprimerAdherent(request, id):
      try:
            adherent = Adherent.objects.get(id=id)
            adherent.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
      except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
@api_view(['PATCH'])
def modifierAdherent(request, id):
      try:
            adherent = Adherent.objects.get(id=id)
      
            serializer = AdherentSerialize(instance=adherent, data=request.data , partial=True)
            
            if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
      

@api_view(['POST'])
def ajouterLivre(request):
      try:
            
            serializer = LivreSerialize(data=request.data)
           
            if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data, status=201)
            return Response(serializer.errors)

      except Exception as e:
            return Response(str(e) , status=status.HTTP_400_BAD_REQUEST)            
@api_view(['GET'])
def afflivre(request):
      try:
            livres = Livre.objects.order_by('titreLivre').all()
            serializer = LivreSerialize(livres, many=True)
            return Response(serializer.data)
      except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)      
@api_view(['GET'])
def affichelivrebyid(request,id):
      try:
            livre = Livre.objects.get(id=id)
            serializer = LivreSerialize(livre)
            return Response(serializer.data)
      except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)      
@api_view(['DELETE'])
def deletelivre(request,id):
      try:
            livre = Livre.objects.get(id=id)
            livre.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
      except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def updatelivre(request,id):
      try:
            livre = Livre.objects.get(id=id)
            serializer = LivreSerialize(instance=livre, data=request.data , partial=True)
            if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)            
@api_view(['POST'])
def ajouterAuteur(request):
      try:
            serializer=AutorSerialize(data=request.data)
            if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors)
      except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST) 
      
@api_view(['GET'])
def affauteur(request):
      try:
            auteurs=Auteur.objects.order_by('nomAuteur').all()
            serializer=AutorSerialize(auteurs,many=True)
            return Response(serializer.data)
      except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)      
@api_view(['GET'])
def getNameAuteur(request,id):
      try:
            auteur=Auteur.objects.get(id=id)
            serializer=AutorSerialize(auteur)
            return Response(serializer.data['nomAuteur']+" "+serializer.data['prenomAuteur'] )
      except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)      

@api_view(['GET'])
def getauteurByid(request,id):
      try:
            auteur=Auteur.objects.get(id=id)
            serializer=AutorSerialize(auteur)
            return Response(serializer.data)
      except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)      
@api_view(['DELETE'])
def deleteAuteur(request,id):
      try:
            auteur=Auteur.objects.get(id=id)
            auteur.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
      except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def ajouterEmprunt(request):
      try:
            livreId=request.data['livre']
            print(livreId)
            serializer = EmpruntSerialize(data=request.data)
            if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data, status=201)
            return Response(serializer.errors)

      except Exception as e:
            return Response(str(e) , status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def afficherToutesEmprunt(request):
      try:
            emprunts = Emprunt.objects.all()
            serializer = EmpruntSerialize(emprunts, many=True)
            return Response(serializer.data)
      except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def supprimerEmprunt(request, id):
      try:
            emprunt = Emprunt.objects.get(id=id)
            emprunt.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
      except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def updateEmprunt(request,id):
      try:
            emprunt = Emprunt.objects.get(id=id)
            serializer = EmpruntSerialize(instance=emprunt, data=request.data , partial=True)
            if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)      
@api_view(['PATCH'])
def reTourLivre(request,id):
      try:
            emprunt = Emprunt.objects.get(id=id)
                   
            today=date.today()
            emprunt.date_retour_effectif=today
            serializer = EmpruntSerialize(instance=emprunt, data=request.data , partial=True)
            if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)        
@api_view(['GET'])
def retrieve_retard(self):
        today = date.today()
        emprunts = Emprunt.objects.filter(date_retour_prevu__lt=today)
        serializer=EmpruntSerialize(instance=emprunts,many=True)
        return Response(serializer.data)

    # views.py
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmpruntSerialize

class EmpruntViewSet(viewsets.ModelViewSet):
    queryset = Emprunt.objects.all()
    serializer_class = EmpruntSerialize

   
