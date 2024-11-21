from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Offre
from .forms import UserRegistrationForm

# Tests pour les offres
class OffreTests(TestCase):
    def setUp(self):
        # Créez des offres pour tester
        self.offre_solo = Offre.objects.create(
            nom="Offre Solo",
            description="Accès pour une personne",
            prix=50.00,
            nombre_de_places=1
        )

    def test_offre_list_view(self):
        # Vérifie si la page des offres renvoie un statut 200
        response = self.client.get(reverse('liste_offres'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Offre Solo")
    
    def test_offre_detail_view(self):
        # Vérifie si le détail d'une offre fonctionne correctement
        response = self.client.get(reverse('ajouter_au_panier', args=[self.offre_solo.id]))
        self.assertEqual(response.status_code, 302)  # Redirection attendue pour les POST
    
    def test_panier_initialement_vide(self):
        # Vérifie que le panier est initialement vide
        session = self.client.session
        self.assertNotIn('panier', session)

    def test_ajout_au_panier(self):
        # Ajoute une offre au panier et vérifie si elle y est
        response = self.client.post(reverse('ajouter_au_panier', args=[self.offre_solo.id]))
        self.assertEqual(response.status_code, 302)  # Redirection attendue après ajout
        session = self.client.session
        self.assertIn(self.offre_solo.id, session.get('panier', []))
    
    def test_voir_panier_contenu(self):
        # Ajoute une offre au panier et vérifie son affichage
        session = self.client.session
        session['panier'] = [self.offre_solo.id]
        session.save()
        response = self.client.get(reverse('voir_panier'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Offre Solo")
    
    def test_suppression_du_panier(self):
        # Supprime une offre du panier et vérifie si elle est bien supprimée
        session = self.client.session
        session['panier'] = [self.offre_solo.id]
        session.save()
        response = self.client.post(reverse('supprimer_du_panier', args=[self.offre_solo.id]))
        self.assertEqual(response.status_code, 302)  # Redirection attendue après suppression
        session = self.client.session
        self.assertNotIn(self.offre_solo.id, session.get('panier', []))

# Tests pour les formulaires
class FormTests(TestCase):
    def test_inscription_form_valide(self):
        # Vérifie qu'un formulaire valide passe
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',  # Ajout du champ requis
            'password1': 'SecurePass123!',
            'password2': 'SecurePass123!'
        }
        form = UserRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid(), msg=form.errors)  # Ajout des erreurs pour le debug

    def test_inscription_form_invalide(self):
        # Vérifie qu'un formulaire invalide est rejeté
        form_data = {
            'username': 'testuser',
            'password1': 'SecurePass123!',
            'password2': 'WrongPass456!'
        }
        form = UserRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    def test_inscription_form_champ_vide(self):
        # Vérifie qu'un formulaire avec des champs vides est rejeté
        form_data = {
            'username': '',
            'password1': '',
            'password2': ''
        }
        form = UserRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('password1', form.errors)
        self.assertIn('password2', form.errors)

# Tests pour les accès protégés
class AccessTests(TestCase):
    def setUp(self):
        # Créer un utilisateur de test
        self.user = User.objects.create_user(username='testuser', password='SecurePass123!')

    def test_acces_page_profil_non_connecte(self):
        # Vérifie qu'un utilisateur non connecté est redirigé
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('profile')}")

    def test_acces_page_profil_connecte(self):
        # Vérifie qu'un utilisateur connecté peut accéder à la page de profil
        self.client.login(username='testuser', password='SecurePass123!')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Profil")

# Tests pour les erreurs
class ErrorTests(TestCase):
    def test_page_inexistante(self):
        # Vérifie qu'une page inexistante renvoie une erreur 404
        response = self.client.get('/page-inexistante/')
        self.assertEqual(response.status_code, 404)

    def test_ajout_offre_inexistante(self):
        # Vérifie qu'une tentative d'ajouter une offre inexistante renvoie une erreur 404
        response = self.client.post(reverse('ajouter_au_panier', args=[999]))
        self.assertEqual(response.status_code, 404)

# Tests de performance
class PerformanceTests(TestCase):
    def setUp(self):
        # Création d'une offre pour les tests
        self.offre_solo = Offre.objects.create(
            nom="Offre Solo",
            description="Accès pour une personne",
            prix=50.00,
            nombre_de_places=1
        )

    def test_liste_offres_performance(self):
        import time
        start_time = time.time()
        response = self.client.get(reverse('liste_offres'))
        end_time = time.time()
        self.assertEqual(response.status_code, 200)
        self.assertLess(end_time - start_time, 0.5)
