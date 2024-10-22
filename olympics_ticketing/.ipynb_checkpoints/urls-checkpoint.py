from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reservations/', include('reservations.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Ajout des URLs de connexion
]

    