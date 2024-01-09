from django.urls import path
from . import views

urlpatterns=[
    path('add/', views.ajouterAuteur),
    path('affauteur/', views.affauteur),
    path('getauteurByid/<int:id>',views.getauteurByid),
    path('getnameAuteur/<int:id>',views.getNameAuteur)
]