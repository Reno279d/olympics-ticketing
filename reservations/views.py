from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Offre
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required

def liste_offres(request):
    # Compte des articles dans le panier
    panier = request.session.get('panier', [])
    panier_count = len(panier)

    offres = Offre.objects.all()
    return render(request, 'offres.html', {'offres': offres, 'panier_count': panier_count})

def ajouter_au_panier(request, offre_id):
    if request.method == 'POST':
        offre = get_object_or_404(Offre, id=offre_id)
        panier = request.session.get('panier', [])
        panier.append(offre_id)
        request.session['panier'] = panier

        # Vérifier si la requête est AJAX
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            panier_count = len(panier)
            return JsonResponse({'message': 'Offre ajoutée au panier', 'panier_count': panier_count}, status=200)

    # Redirection normale si ce n'est pas une requête AJAX
    return redirect('voir_panier')

def voir_panier(request):
    panier = request.session.get('panier', [])
    offres = Offre.objects.filter(id__in=panier)
    return render(request, 'voir_panier.html', {'offres': offres})

def supprimer_du_panier(request, offre_id):
    panier = request.session.get('panier', [])
    panier.remove(offre_id)
    request.session['panier'] = panier
    return redirect('voir_panier')

# Gestion de l'inscription
def inscription(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige vers la page de connexion après inscription
    else:
        form = UserRegistrationForm()
    return render(request, 'inscription.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'profile.html')

