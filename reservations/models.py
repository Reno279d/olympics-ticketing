from django.db import models
from django.contrib.auth.models import User

class Offre(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    nombre_de_places = models.IntegerField()

    def __str__(self):
        return self.nom

class Billet(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    offre = models.ForeignKey(Offre, on_delete=models.CASCADE)
    qr_code = models.CharField(max_length=255, unique=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Billet pour {self.utilisateur} - {self.offre}"
    