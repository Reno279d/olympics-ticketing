from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Route pour l'administration Django
    path('admin/', admin.site.urls),

    # Routes pour l'application "reservations"
    path('reservations/', include('reservations.urls')),  

    # Routes pour le système d'authentification de Django
    path('accounts/', include('django.contrib.auth.urls')),  

    # Route principale redirigée vers l'application "reservations"
    path('', include('reservations.urls')),  
]

# Configuration des fichiers statiques en mode DEBUG uniquement
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
