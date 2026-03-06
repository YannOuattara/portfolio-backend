from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from .models import Localisation, Projet, Experience, Service, PriseDeContact, ReseauSocial


class LocalisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localisation
        fields = [
            'id', 'user', 'ville', 'pays', 'region',
            'latitude', 'longitude', 'google_maps_url',
        ]


class ReseauSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReseauSocial
        fields = [
            'id', 'user', 'plateforme', 'url', 'icone', 'ordre', 'actif',
        ]


class ProjetSerializer(serializers.ModelSerializer):
    icone_categorie = serializers.SerializerMethodField()
    periode_affichage = serializers.SerializerMethodField()

    class Meta:
        model = Projet
        fields = [
            'id', 'user', 'titre', 'description_courte', 'description_longue',
            'categorie', 'statut', 'technologies', 'image',
            'url_github', 'url_live', 'url_demo',
            'en_vedette', 'ordre', 'date_debut', 'date_fin',
            'icone_categorie', 'periode_affichage',
        ]

    @extend_schema_field(serializers.CharField())
    def get_icone_categorie(self, obj):
        icones = {
            'fullstack': 'fas fa-layer-group',
            'backend': 'fas fa-server',
            'frontend': 'fas fa-desktop',
            'data': 'fas fa-chart-bar',
            'odoo': 'fas fa-cogs',
            'mobile': 'fas fa-mobile-alt',
            'autre': 'fas fa-code',
        }
        return icones.get(obj.categorie, 'fas fa-code')

    @extend_schema_field(serializers.CharField())
    def get_periode_affichage(self, obj):
        debut = str(obj.date_debut.year) if obj.date_debut else ''
        fin = str(obj.date_fin.year) if obj.date_fin else ''
        if debut and fin:
            return f"{debut} — {fin}"
        return debut or fin or ''


class ExperienceSerializer(serializers.ModelSerializer):
    periode = serializers.CharField(read_only=True)

    class Meta:
        model = Experience
        fields = [
            'id', 'user', 'type', 'titre', 'organisation',
            'description', 'date_debut', 'date_fin',
            'lieu', 'technologies', 'ordre', 'actuel', 'periode',
        ]


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            'id', 'user', 'titre', 'description', 'icone',
            'numero', 'technologies', 'ordre', 'actif',
        ]


class PriseDeContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriseDeContact
        fields = [
            'id', 'user', 'nom', 'email', 'sujet', 'message',
            'statut', 'ip_address', 'date_envoi', 'date_lecture',
        ]
        read_only_fields = ['statut', 'ip_address', 'date_envoi', 'date_lecture']

    def validate_email(self, value):
        return value.lower()

    def validate_message(self, value):
        if len(value.strip()) < 10:
            raise serializers.ValidationError(
                "Le message doit contenir au moins 10 caractères."
            )
        return value