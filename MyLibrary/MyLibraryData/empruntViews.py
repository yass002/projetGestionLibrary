from . import views
from django.urls import path

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmpruntViewSet


router = DefaultRouter()
router.register(r'emprunts', EmpruntViewSet)

urlpatterns=[
  
    path('', include(router.urls)),
    path('getretard/',views.retrieve_retard )

]