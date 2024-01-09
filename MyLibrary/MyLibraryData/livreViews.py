from . import views
from django.urls import path


urlpatterns=[
    path('add/', views.ajouterLivre),
    path('afflivre/', views.afflivre),
    path('affichelivrebyid/<int:id>', views.affichelivrebyid),
    path('deletelivre/<int:id>', views.deletelivre),
    path('update/<int:id>', views.updatelivre)

]