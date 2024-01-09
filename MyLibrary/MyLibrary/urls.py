
from django.contrib import admin
from django.urls import path,include

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path("adherent/" , include('MyLibraryData.urls')),
    path("livre/",include('MyLibraryData.livreViews')),
    path("auteur/" , include('MyLibraryData.autorViews')),
    path("api/" , include('MyLibraryData.empruntViews'))
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
