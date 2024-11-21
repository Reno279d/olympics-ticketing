from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# Déclarez d'abord urlpatterns avant d'ajouter les fichiers statiques
urlpatterns = [
    path('', views.accueil, name='accueil'),  # Page d'accueil
    path('offres/', views.liste_offres, name='liste_offres'),
    path('ajouter-au-panier/<int:offre_id>/', views.ajouter_au_panier, name='ajouter_au_panier'),
    path('panier/', views.voir_panier, name='voir_panier'),
    path('supprimer-du-panier/<int:offre_id>/', views.supprimer_du_panier, name='supprimer_du_panier'),
    path('inscription/', views.inscription, name='inscription'),
    path('profile/', views.profile, name='profile'),
]

# Ajoutez les fichiers statiques si DEBUG est désactivé
if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
