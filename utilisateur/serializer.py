from rest_framework import serializers
from .models import Utilisateur
from portfolio.serializer import (
    ProjetSerializer,
    ExperienceSerializer,
    ServiceSerializer,
    ReseauSocialSerializer,
    LocalisationSerializer,
)


# Version légère pour les listes
class UtilisateurListSerializer(serializers.ModelSerializer):
    nom_complet = serializers.CharField(read_only=True)

    class Meta:
        model = Utilisateur
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'nom_complet', 'titre', 'telephone', 'disponible',
            'photo_de_profile',
        ]


# Version complète avec toutes les relations imbriquées
class UtilisateurDetailSerializer(serializers.ModelSerializer):
    nom_complet = serializers.CharField(read_only=True)
    projects = ProjetSerializer(many=True, read_only=True)
    experiences = ExperienceSerializer(many=True, read_only=True)
    services = ServiceSerializer(many=True, read_only=True)
    social_networks = ReseauSocialSerializer(many=True, read_only=True)
    locations = LocalisationSerializer(many=True, read_only=True)

    class Meta:
        model = Utilisateur
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'nom_complet', 'titre', 'sous_titre', 'description',
            'telephone', 'photo_de_profile', 'lien_cv',
            'disponible', 'annees_experience', 'nombre_projets',
            'projects', 'experiences', 'services',
            'social_networks', 'locations',
        ]


# Alias pour rétrocompatibilité avec les vues existantes
UtilisateurSerializer = UtilisateurListSerializer