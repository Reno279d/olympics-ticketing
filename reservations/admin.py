from django.contrib import admin
from .models import Offre, Billet

@admin.register(Offre)
class OffreAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'prix', 'nombre_de_places')  # Colonnes affichées
    search_fields = ('nom', 'description')  # Barre de recherche
    list_filter = ('prix',)  # Filtres par prix

@admin.register(Billet)
class BilletAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'offre', 'qr_code', 'date_creation')  # Colonnes affichées
    search_fields = ('qr_code', 'utilisateur__username')  # Recherche par QR code ou nom d'utilisateur
    list_filter = ('date_creation',)  # Filtre par date de création
