from django.db import models
from django.conf import settings


class Localisation(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Utilisateur",
        related_name="locations",
        null=True,
        blank=True,
    )
    ville = models.CharField(max_length=100, verbose_name="Ville")
    pays = models.CharField(max_length=100, verbose_name="Pays")
    region = models.CharField(max_length=100, blank=True, null=True, verbose_name="Région")
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True, verbose_name="Latitude"
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True, verbose_name="Longitude"
    )
    google_maps_url = models.URLField(blank=True, null=True, verbose_name="Lien Google Maps")

    def __str__(self):
        return f"{self.ville}, {self.pays}"

    class Meta:
        verbose_name = "Localisation"
        verbose_name_plural = "Localisations"


class Projet(models.Model):
    CATEGORIE_CHOICES = [
        ('fullstack', 'Full Stack'),
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
        ('data', 'Data / IA'),
        ('odoo', 'Odoo'),
        ('mobile', 'Mobile'),
        ('autre', 'Autre'),
    ]
    STATUT_CHOICES = [
        ('en_cours', 'En cours'),
        ('termine', 'Terminé'),
        ('archive', 'Archivé'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Utilisateur",
        related_name="projects",
        null=True,
        blank=True,
    )
    titre = models.CharField(max_length=150, verbose_name="Titre")
    description_courte = models.CharField(max_length=300, verbose_name="Description courte")
    description_longue = models.TextField(blank=True, null=True, verbose_name="Description longue")
    categorie = models.CharField(
        max_length=20, choices=CATEGORIE_CHOICES, default='autre', verbose_name="Catégorie"
    )
    statut = models.CharField(
        max_length=20, choices=STATUT_CHOICES, default='termine', verbose_name="Statut"
    )
    technologies = models.JSONField(default=list, verbose_name="Technologies utilisées")
    image = models.ImageField(
        upload_to='projets/', blank=True, null=True, verbose_name="Image"
    )
    url_github = models.URLField(blank=True, null=True, verbose_name="Lien GitHub")
    url_live = models.URLField(blank=True, null=True, verbose_name="Lien Live")
    url_demo = models.URLField(blank=True, null=True, verbose_name="Lien Démo")
    en_vedette = models.BooleanField(default=False, verbose_name="En vedette")
    ordre = models.PositiveIntegerField(default=0, verbose_name="Ordre d'affichage")
    date_debut = models.DateField(blank=True, null=True, verbose_name="Date de début")
    date_fin = models.DateField(blank=True, null=True, verbose_name="Date de fin")

    def __str__(self):
        return self.titre

    class Meta:
        verbose_name = "Projet"
        verbose_name_plural = "Projets"
        ordering = ['ordre', '-date_fin']


class Experience(models.Model):
    TYPE_CHOICES = [
        ('education', 'Formation'),
        ('professionnel', 'Expérience professionnelle'),
        ('projet', 'Projet'),
        ('competition', 'Compétition'),
        ('certification', 'Certification'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Utilisateur",
        related_name="experiences",
        null=True,
        blank=True,
    )
    type = models.CharField(
        max_length=20, choices=TYPE_CHOICES, default='education', verbose_name="Type"
    )
    titre = models.CharField(max_length=200, verbose_name="Titre / Diplôme / Poste")
    organisation = models.CharField(max_length=200, verbose_name="Organisation / École / Entreprise")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    date_debut = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Date de début (ex: 2023)"
    )
    date_fin = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Date de fin (ex: 2024 ou Présent)"
    )
    lieu = models.CharField(max_length=150, blank=True, null=True, verbose_name="Lieu")
    technologies = models.JSONField(default=list, verbose_name="Technologies / Outils")
    ordre = models.PositiveIntegerField(default=0, verbose_name="Ordre d'affichage")
    actuel = models.BooleanField(
        default=False, verbose_name="En cours (date_fin = Présent)"
    )

    @property
    def periode(self):
        debut = self.date_debut or ''
        fin = 'Présent' if self.actuel else (self.date_fin or '')
        if debut and fin:
            return f"{debut} — {fin}"
        return debut or fin or ''

    def __str__(self):
        return f"{self.titre} — {self.organisation}"

    class Meta:
        verbose_name = "Expérience / Formation"
        verbose_name_plural = "Expériences / Formations"
        ordering = ['ordre', '-date_debut']


class Service(models.Model):
    ICONE_CHOICES = [
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
        ('data', 'Data / IA'),
        ('security', 'Sécurité'),
        ('devops', 'DevOps'),
        ('mobile', 'Mobile'),
        ('autre', 'Autre'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Utilisateur",
        related_name="services",
        null=True,
        blank=True,
    )
    titre = models.CharField(max_length=150, verbose_name="Titre du service")
    description = models.TextField(verbose_name="Description")
    icone = models.CharField(
        max_length=20, choices=ICONE_CHOICES, default='autre', verbose_name="Icône / Catégorie"
    )
    numero = models.PositiveIntegerField(default=1, verbose_name="Numéro")
    technologies = models.JSONField(default=list, verbose_name="Technologies / Outils")
    ordre = models.PositiveIntegerField(default=0, verbose_name="Ordre d'affichage")
    actif = models.BooleanField(default=True, verbose_name="Actif")

    def __str__(self):
        return self.titre

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ['ordre']


class PriseDeContact(models.Model):
    STATUT_CHOICES = [
        ('nouveau', 'Nouveau'),
        ('lu', 'Lu'),
        ('repondu', 'Répondu'),
        ('archive', 'Archivé'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Destinataire",
        related_name="contacts_recus",
        null=True,
        blank=True,
    )
    nom = models.CharField(max_length=100, verbose_name="Nom complet")
    email = models.EmailField(verbose_name="Email")
    sujet = models.CharField(max_length=200, verbose_name="Sujet")
    message = models.TextField(verbose_name="Message")
    statut = models.CharField(
        max_length=20, choices=STATUT_CHOICES, default='nouveau', verbose_name="Statut"
    )
    ip_address = models.GenericIPAddressField(
        blank=True, null=True, verbose_name="Adresse IP"
    )
    date_envoi = models.DateTimeField(auto_now_add=True, verbose_name="Date d'envoi")
    date_lecture = models.DateTimeField(
        blank=True, null=True, verbose_name="Date de lecture"
    )

    def __str__(self):
        return f"{self.nom} — {self.sujet}"

    class Meta:
        verbose_name = "Message de contact"
        verbose_name_plural = "Messages de contact"
        ordering = ['-date_envoi']


class ReseauSocial(models.Model):
    PLATEFORME_CHOICES = [
        ('github', 'GitHub'),
        ('linkedin', 'LinkedIn'),
        ('twitter', 'Twitter / X'),
        ('instagram', 'Instagram'),
        ('youtube', 'YouTube'),
        ('autre', 'Autre'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Utilisateur",
        related_name="social_networks",
        null=True,
        blank=True,
    )
    plateforme = models.CharField(
        max_length=20, choices=PLATEFORME_CHOICES, default='autre', verbose_name="Plateforme"
    )
    url = models.URLField(verbose_name="URL du profil")
    icone = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Classe icône (ex: fab fa-github)"
    )
    ordre = models.PositiveIntegerField(default=0, verbose_name="Ordre d'affichage")
    actif = models.BooleanField(default=True, verbose_name="Actif")

    def __str__(self):
        return f"{self.get_plateforme_display()} — {self.user}"

    class Meta:
        verbose_name = "Réseau social"
        verbose_name_plural = "Réseaux sociaux"
        ordering = ['ordre']