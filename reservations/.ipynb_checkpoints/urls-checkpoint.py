from django.urls import path
from . import views

urlpatterns = [
    path('offres/', views.liste_offres, name='liste_offres'),
    path('ajouter-au-panier/<int:offre_id>/', views.ajouter_au_panier, name='ajouter_au_panier'),
    path('panier/', views.voir_panier, name='voir_panier'),
    path('supprimer-du-panier/<int:offre_id>/', views.supprimer_du_panier, name='supprimer_du_panier'),
    path('inscription/', views.inscription, name='inscription'),
    path('profile/', views.profile, name='profile'),
]
