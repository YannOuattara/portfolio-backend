from django.contrib import admin
from .models import Localisation, Projet, Experience, Service, PriseDeContact, ReseauSocial


# ── Inlines pour l'admin Utilisateur ─────────────────────────────────────────

class ProjetInline(admin.TabularInline):
    model = Projet
    extra = 0
    fields = ('titre', 'categorie', 'statut', 'en_vedette', 'ordre')


class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 0
    fields = ('type', 'titre', 'organisation', 'date_debut', 'date_fin', 'actuel')


class ServiceInline(admin.TabularInline):
    model = Service
    extra = 0
    fields = ('titre', 'icone', 'ordre', 'actif')


class ReseauSocialInline(admin.TabularInline):
    model = ReseauSocial
    extra = 0
    fields = ('plateforme', 'url', 'ordre', 'actif')


class LocalisationInline(admin.TabularInline):
    model = Localisation
    extra = 0
    fields = ('ville', 'pays', 'region')


# ── Modèles enregistrés ───────────────────────────────────────────────────────

@admin.register(Localisation)
class LocalisationAdmin(admin.ModelAdmin):
    list_display = ('ville', 'pays', 'region', 'user')
    list_filter = ('pays',)
    search_fields = ('ville', 'pays', 'user__username')


@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'statut', 'en_vedette', 'ordre', 'user')
    list_filter = ('categorie', 'statut', 'en_vedette')
    search_fields = ('titre', 'description_courte')
    list_editable = ('en_vedette', 'ordre', 'statut')
    ordering = ('ordre',)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('titre', 'organisation', 'type', 'date_debut', 'date_fin', 'actuel', 'user')
    list_filter = ('type', 'actuel')
    search_fields = ('titre', 'organisation')
    list_editable = ('ordre',) if False else ()  # ordre si besoin
    ordering = ('ordre',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('titre', 'icone', 'numero', 'ordre', 'actif', 'user')
    list_filter = ('icone', 'actif')
    search_fields = ('titre',)
    list_editable = ('actif', 'ordre')
    ordering = ('ordre',)


@admin.register(PriseDeContact)
class PriseDeContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'sujet', 'statut', 'date_envoi', 'ip_address')
    list_filter = ('statut',)
    search_fields = ('nom', 'email', 'sujet')
    readonly_fields = ('nom', 'email', 'sujet', 'message', 'ip_address', 'date_envoi', 'date_lecture')
    ordering = ('-date_envoi',)

    def has_add_permission(self, request):
        return False


@admin.register(ReseauSocial)
class ReseauSocialAdmin(admin.ModelAdmin):
    list_display = ('plateforme', 'url', 'ordre', 'actif', 'user')
    list_filter = ('plateforme', 'actif')
    list_editable = ('actif', 'ordre')
    ordering = ('ordre',)
