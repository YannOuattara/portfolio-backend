from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Peupler la base de données avec les données du portfolio'

    def handle(self, *args, **options):
        User = get_user_model()

        # ── Profil ──────────────────────────────────────────────────────────
        user = User.objects.filter(username='admin').first()
        if not user:
            self.stdout.write('Utilisateur admin introuvable.')
            return

        user.first_name = 'Yann Cédric Emmanuel'
        user.last_name = 'Ouattara'
        user.email = 'yanncedricemmanuelo@gmail.com'
        user.titre = 'Étudiant L3 Computer Science'
        user.sous_titre = 'Python • Django • Angular • Odoo • Flutter'
        user.description = (
            "Je suis étudiant en 3ᵉ année de génie logiciel, passionné par le développement web "
            "et la création de solutions numériques innovantes. J'aime relever des défis techniques, "
            "apprendre continuellement et transformer des idées en applications concrètes. "
            "En dehors du code, je suis un amateur de jeux vidéo et une personne très engagée "
            "dans le travail et la progression personnelle."
        )
        user.telephone = '+225 07 69 64 74 02'
        user.disponible = True
        user.annees_experience = 2
        user.nombre_projets = 4
        user.save()
        self.stdout.write('✓ Profil mis à jour')

        # ── Localisation ─────────────────────────────────────────────────────
        from portfolio.models import Localisation
        Localisation.objects.get_or_create(
            user=user, ville='Abidjan',
            defaults={'pays': "Côte d'Ivoire", 'region': 'Lagunes'}
        )
        self.stdout.write('✓ Localisation créée')

        # ── Réseaux sociaux ──────────────────────────────────────────────────
        from portfolio.models import ReseauSocial
        reseaux = [
            {'plateforme': 'github', 'url': 'https://github.com/YannOuattara', 'icone': 'fab fa-github', 'ordre': 1},
            {'plateforme': 'linkedin', 'url': 'https://www.linkedin.com/in/yann-c%C3%A9dric-emmanuel-ouattara-5b0249392/', 'icone': 'fab fa-linkedin', 'ordre': 2},
        ]
        for r in reseaux:
            ReseauSocial.objects.get_or_create(user=user, plateforme=r['plateforme'], defaults={
                'url': r['url'], 'icone': r['icone'], 'ordre': r['ordre'], 'actif': True
            })
        self.stdout.write('✓ Réseaux sociaux créés')

        # ── Formations ───────────────────────────────────────────────────────
        from portfolio.models import Experience
        formations = [
            {'titre': 'Licence 3 Computer Science (en cours)', 'organisation': 'Institut Ivoirien de Technologie de Grand Bassam', 'date_debut': '2025', 'date_fin': '2026', 'actuel': True, 'ordre': 1},
            {'titre': 'Licence 2 Computer Science', 'organisation': 'Institut Ivoirien de Technologie de Grand Bassam', 'date_debut': '2024', 'date_fin': '2025', 'actuel': False, 'ordre': 2},
            {'titre': 'Licence 1 Computer Science', 'organisation': 'Institut Ivoirien de Technologie de Grand Bassam', 'date_debut': '2023', 'date_fin': '2024', 'actuel': False, 'ordre': 3},
            {'titre': 'Baccalauréat série C', 'organisation': 'Cours Secondaire Méthodiste de Cocody', 'date_debut': '2020', 'date_fin': '2021', 'actuel': False, 'ordre': 4},
        ]
        for f in formations:
            Experience.objects.get_or_create(
                user=user, titre=f['titre'], type='education',
                defaults={
                    'organisation': f['organisation'],
                    'date_debut': f['date_debut'],
                    'date_fin': f['date_fin'],
                    'actuel': f['actuel'],
                    'ordre': f['ordre'],
                    'lieu': 'Abidjan, Côte d\'Ivoire',
                    'technologies': [],
                }
            )
        self.stdout.write('✓ Formations créées')

        # ── Expériences professionnelles ─────────────────────────────────────
        experiences = [
            {
                'titre': 'Développeur Web – Projet E-commerce (Vente de véhicules)',
                'organisation': 'Projet académique',
                'description': 'Conception et développement d\'une application web e-commerce. Gestion des utilisateurs, annonces de véhicules et commandes. Développement du backend et intégration frontend (HTML/CSS).',
                'technologies': ['Python', 'Django', 'HTML', 'CSS'],
                'date_debut': '2024', 'date_fin': '2024', 'ordre': 1,
            },
            {
                'titre': 'Développeur Java – Gestion de cantine scolaire',
                'organisation': 'Projet académique',
                'description': 'Application de gestion des élèves, repas et paiements.',
                'technologies': ['Java'],
                'date_debut': '2024', 'date_fin': '2024', 'ordre': 2,
            },
            {
                'titre': 'Développeur Odoo – Modules métiers sous Odoo 18',
                'organisation': 'Projet académique',
                'description': 'Module Estate : gestion de biens immobiliers. Module Parc Informatique : gestion de matériel IT. Création de modèles, vues et logique métier personnalisé.',
                'technologies': ['Odoo', 'Python', 'XML'],
                'date_debut': '2025', 'date_fin': '2025', 'ordre': 3,
            },
            {
                'titre': 'Développeur C# – Gestion universitaire',
                'organisation': 'Projet académique',
                'description': 'Gestion de la trésorerie. Gestion des étudiants et des inscriptions.',
                'technologies': ['C#', '.NET'],
                'date_debut': '2024', 'date_fin': '2024', 'ordre': 4,
            },
        ]
        for e in experiences:
            Experience.objects.get_or_create(
                user=user, titre=e['titre'], type='professionnel',
                defaults={
                    'organisation': e['organisation'],
                    'description': e['description'],
                    'technologies': e['technologies'],
                    'date_debut': e['date_debut'],
                    'date_fin': e['date_fin'],
                    'actuel': False,
                    'ordre': e['ordre'],
                    'lieu': 'Abidjan, Côte d\'Ivoire',
                }
            )
        self.stdout.write('✓ Expériences créées')

        # ── Projets ──────────────────────────────────────────────────────────
        from portfolio.models import Projet
        projets = [
            {
                'titre': 'DriveShop',
                'description_courte': 'Plateforme e-commerce de vente de véhicules',
                'description_longue': 'Application web e-commerce destinée à la vente de véhicules. Gestion des utilisateurs, annonces et commandes. Backend Django, frontend HTML/CSS.',
                'categorie': 'fullstack',
                'technologies': ['Python', 'Django', 'HTML', 'CSS'],
                'url_github': 'https://github.com/YannOuattara',
                'ordre': 1,
            },
            {
                'titre': 'IT Park',
                'description_courte': 'Module Odoo pour la gestion d\'un parc informatique',
                'description_longue': 'Module métier sous Odoo 18 pour la gestion d\'un parc informatique pour prestataire IT. Gestion du matériel, des interventions et des clients.',
                'categorie': 'odoo',
                'technologies': ['Odoo', 'Python', 'XML'],
                'url_github': 'https://github.com/YannOuattara',
                'ordre': 2,
            },
            {
                'titre': 'ArchiSchool',
                'description_courte': 'Système de gestion des archives d\'une école',
                'description_longue': 'Application de gestion des archives scolaires : documents, élèves, inscriptions et historiques.',
                'categorie': 'backend',
                'technologies': ['Python', 'Django'],
                'url_github': 'https://github.com/YannOuattara',
                'ordre': 3,
            },
            {
                'titre': 'Hospital Management',
                'description_courte': 'Module Odoo pour la gestion d\'un centre hospitalier',
                'description_longue': 'Module métier sous Odoo 18 pour la gestion d\'un centre hospitalier : patients, consultations, médecins et facturation.',
                'categorie': 'odoo',
                'technologies': ['Odoo', 'Python', 'XML'],
                'url_github': 'https://github.com/YannOuattara',
                'ordre': 4,
            },
        ]
        for p in projets:
            Projet.objects.get_or_create(
                user=user, titre=p['titre'],
                defaults={
                    'description_courte': p['description_courte'],
                    'description_longue': p['description_longue'],
                    'categorie': p['categorie'],
                    'technologies': p['technologies'],
                    'url_github': p['url_github'],
                    'statut': 'termine',
                    'en_vedette': True,
                    'ordre': p['ordre'],
                }
            )
        self.stdout.write('✓ Projets créés')

        self.stdout.write(self.style.SUCCESS('\n✅ Base de données peuplée avec succès !'))
