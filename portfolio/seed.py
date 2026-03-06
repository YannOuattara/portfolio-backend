"""
Seed — données initiales du portfolio de Ouattara Yann Cédric Emmanuel.
Usage :
    python manage.py shell < portfolio/seed.py
"""

import os
import sys
import django

# Permettre l'exécution directe (python portfolio/seed.py)
if __name__ == '__main__':
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolioAngularBackend.settings')
    django.setup()

from django.contrib.auth import get_user_model
from portfolio.models import Localisation, Projet, Experience, Service, PriseDeContact, ReseauSocial

Utilisateur = get_user_model()

print("Nettoyage des tables...")
PriseDeContact.objects.all().delete()
ReseauSocial.objects.all().delete()
Service.objects.all().delete()
Experience.objects.all().delete()
Projet.objects.all().delete()
Localisation.objects.all().delete()
Utilisateur.objects.filter(is_superuser=False).delete()

# ── Utilisateur principal ─────────────────────────────────────────────────────
print("Création de l'utilisateur...")
user = Utilisateur.objects.create_user(
    username='yann',
    email='yanncedricemmanuelo@gmail.com',
    password='admin1234',
    first_name='Yann Cédric Emmanuel',
    last_name='Ouattara',
    titre='Étudiant L3 Computer Science',
    sous_titre='Développeur Web & Logiciel',
    description=(
        "Je suis étudiant en 3ᵉ année de génie logiciel, passionné par le développement web "
        "et la création de solutions numériques innovantes. J'aime relever des défis techniques, "
        "apprendre continuellement et transformer des idées en applications concrètes. "
        "En dehors du code, je suis un amateur de jeux vidéo et une personne très engagée "
        "dans le travail et la progression personnelle."
    ),
    telephone='+225 07 69 64 74 02',
    disponible=True,
    annees_experience=2,
    nombre_projets=4,
)

# ── Localisation ──────────────────────────────────────────────────────────────
print("Création de la localisation...")
Localisation.objects.create(
    user=user,
    ville='Abidjan',
    pays='Côte d\'Ivoire',
    region='Lagunes',
    latitude=5.354,
    longitude=-4.004,
)

# ── Réseaux sociaux ───────────────────────────────────────────────────────────
print("Création des réseaux sociaux...")
ReseauSocial.objects.create(
    user=user,
    plateforme='github',
    url='https://github.com/YannOuattara',
    icone='fab fa-github',
    ordre=1,
    actif=True,
)
ReseauSocial.objects.create(
    user=user,
    plateforme='linkedin',
    url='https://www.linkedin.com/in/yann-cédric-emmanuel-ouattara-5b0249392/',
    icone='fab fa-linkedin',
    ordre=2,
    actif=True,
)

# ── Projets ───────────────────────────────────────────────────────────────────
print("Création des projets...")
Projet.objects.create(
    user=user,
    titre='DriveShop',
    description_courte='E-commerce de vente de véhicules',
    description_longue=(
        'Un projet e-commerce complet destiné à la vente de véhicules. '
        'Permet la gestion du catalogue, des fiches véhicules, et des commandes.'
    ),
    categorie='fullstack',
    statut='termine',
    technologies=['Django', 'Python', 'HTML', 'CSS', 'JavaScript'],
    en_vedette=True,
    ordre=1,
)
Projet.objects.create(
    user=user,
    titre='IT Park',
    description_courte='Module Odoo pour la gestion d\'un parc informatique',
    description_longue=(
        'Module métier développé sous Odoo pour la gestion d\'un parc informatique '
        'destiné à un prestataire IT. Gestion des équipements, maintenances et interventions.'
    ),
    categorie='odoo',
    statut='termine',
    technologies=['Odoo', 'Python', 'XML', 'PostgreSQL'],
    en_vedette=True,
    ordre=2,
)
Projet.objects.create(
    user=user,
    titre='ArchiSchool',
    description_courte='Gestion des archives d\'une école',
    description_longue=(
        'Application de gestion des archives scolaires permettant de stocker, '
        'rechercher et gérer les documents administratifs d\'un établissement.'
    ),
    categorie='backend',
    statut='termine',
    technologies=['Django', 'Python', 'SQLite', 'Bootstrap'],
    en_vedette=False,
    ordre=3,
)
Projet.objects.create(
    user=user,
    titre='Hospital Management',
    description_courte='Module Odoo pour la gestion d\'un centre hospitalier',
    description_longue=(
        'Module métier sous Odoo pour la gestion complète d\'un centre hospitalier : '
        'patients, consultations, rendez-vous, médecins et facturation.'
    ),
    categorie='odoo',
    statut='termine',
    technologies=['Odoo', 'Python', 'XML', 'PostgreSQL'],
    en_vedette=True,
    ordre=4,
)

# ── Formations & Expériences ──────────────────────────────────────────────────
print("Création des formations/expériences...")
Experience.objects.create(
    user=user,
    type='education',
    titre='Licence 3 Computer Science (en cours)',
    organisation='Institut Ivoirien de Technologie de Grand Bassam',
    description='Spécialisation en génie logiciel.',
    date_debut='2025',
    date_fin='2026',
    lieu='Grand Bassam, Côte d\'Ivoire',
    technologies=['Python', 'Django', 'Angular', 'SQL'],
    ordre=1,
    actuel=True,
)
Experience.objects.create(
    user=user,
    type='education',
    titre='Licence 2 Computer Science',
    organisation='Institut Ivoirien de Technologie de Grand Bassam',
    description='Approfondissement en développement logiciel et bases de données.',
    date_debut='2024',
    date_fin='2025',
    lieu='Grand Bassam, Côte d\'Ivoire',
    technologies=['Python', 'Django', 'SQL', 'JavaScript'],
    ordre=2,
    actuel=False,
)
Experience.objects.create(
    user=user,
    type='education',
    titre='Licence 1 Computer Science',
    organisation='Institut Ivoirien de Technologie de Grand Bassam',
    description='Fondamentaux de l\'informatique et de la programmation.',
    date_debut='2023',
    date_fin='2024',
    lieu='Grand Bassam, Côte d\'Ivoire',
    technologies=['Python', 'C', 'HTML', 'CSS'],
    ordre=3,
    actuel=False,
)
Experience.objects.create(
    user=user,
    type='education',
    titre='Baccalauréat série C',
    organisation='Cours Secondaire Méthodiste de Cocody',
    description='Baccalauréat scientifique, série C (Mathématiques et Sciences Physiques).',
    date_debut='2020',
    date_fin='2021',
    lieu='Cocody, Abidjan',
    technologies=[],
    ordre=4,
    actuel=False,
)

# ── Services ──────────────────────────────────────────────────────────────────
print("Création des services...")
Service.objects.create(
    user=user,
    titre='Développement Backend',
    description='Création d\'APIs REST robustes avec Django et DRF. Gestion de bases de données SQL et optimisation des performances.',
    icone='backend',
    numero=1,
    technologies=['Python', 'Django', 'DRF', 'PostgreSQL', 'SQLite'],
    ordre=1,
    actif=True,
)
Service.objects.create(
    user=user,
    titre='Développement Frontend',
    description='Création d\'interfaces modernes et réactives avec Angular et TypeScript.',
    icone='frontend',
    numero=2,
    technologies=['Angular', 'TypeScript', 'SCSS', 'HTML'],
    ordre=2,
    actif=True,
)
Service.objects.create(
    user=user,
    titre='Développement Odoo',
    description='Création de modules métier personnalisés sous Odoo (ERP). Gestion des processus d\'entreprise.',
    icone='autre',
    numero=3,
    technologies=['Odoo', 'Python', 'XML', 'PostgreSQL'],
    ordre=3,
    actif=True,
)

# ── Messages de démo ──────────────────────────────────────────────────────────
print("Création des messages de démo...")
PriseDeContact.objects.create(
    user=user,
    nom='Alice Dupont',
    email='alice.dupont@example.com',
    sujet='Opportunité de stage',
    message='Bonjour, j\'ai vu votre portfolio et je souhaiterais discuter d\'une opportunité de stage dans notre entreprise.',
    statut='lu',
    ip_address='192.168.1.1',
)
PriseDeContact.objects.create(
    user=user,
    nom='Bob Martin',
    email='bob.martin@example.com',
    sujet='Collaboration freelance',
    message='Salut, je cherche un développeur pour un projet freelance. Votre profil correspond exactement à ce que je recherche.',
    statut='nouveau',
    ip_address='10.0.0.1',
)

# ── Résumé ────────────────────────────────────────────────────────────────────
print("\n" + "="*50)
print("Seed terminé avec succès !")
print(f"  Utilisateur  : {Utilisateur.objects.count()}")
print(f"  Localisations: {Localisation.objects.count()}")
print(f"  Projets      : {Projet.objects.count()}")
print(f"  Expériences  : {Experience.objects.count()}")
print(f"  Services     : {Service.objects.count()}")
print(f"  Réseaux      : {ReseauSocial.objects.count()}")
print(f"  Contacts     : {PriseDeContact.objects.count()}")
print("="*50)
print("Identifiants admin : username=yann / password=admin1234")
print("N'oublie pas de créer un superuser : python manage.py createsuperuser")
