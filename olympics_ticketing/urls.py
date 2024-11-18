from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reservations/', include('reservations.urls')),  # Routes de l'application reservations
    path('accounts/', include('django.contrib.auth.urls')),  # Authentification Django

    # Supprimez cette redirection si elle existe :
    # path('', lambda request: HttpResponseRedirect('/reservations/offres/')),

    # Redirige la racine vers la page d'accueil
    path('', include('reservations.urls')),  # L'URL racine pointe maintenant vers les URLs de reservations
]
