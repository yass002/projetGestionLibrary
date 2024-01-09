from django.urls import path

from . import views


urlpatterns = [
    path('add/',views.ajouterAdherent),
    path('affadhs/' , views.afficherToutesAdherent),
    path('getadhbyid/<int:id>',views.afficherAdherent),
    path('deleteadh/<int:id>',views.supprimerAdherent),
    path('updateadh/<int:id>',views.modifierAdherent),
   
]