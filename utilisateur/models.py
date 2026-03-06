from django.db import models
from django.contrib.auth.models import AbstractUser


class Utilisateur(AbstractUser):
    photo_de_profile = models.ImageField(
        upload_to='profil/',
        blank=True,
        null=True,
        verbose_name="Photo de profil"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Bio / Description"
    )
    age = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Âge"
    )
    lien_cv = models.FileField(
        upload_to='cv/',
        blank=True,
        null=True,
        verbose_name="CV (fichier)"
    )
    telephone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Téléphone"
    )
    titre = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name="Titre professionnel"
    )
    sous_titre = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Sous-titre"
    )
    disponible = models.BooleanField(
        default=True,
        verbose_name="Disponible (stage / freelance / CDI)"
    )
    annees_experience = models.PositiveIntegerField(
        default=0,
        verbose_name="Années d'expérience"
    )
    nombre_projets = models.PositiveIntegerField(
        default=0,
        verbose_name="Nombre de projets réalisés"
    )

    @property
    def nom_complet(self):
        return f"{self.first_name} {self.last_name}".strip() or self.username

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"

    def __str__(self):
        return self.username
