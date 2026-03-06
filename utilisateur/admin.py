from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Utilisateur

@admin.register(Utilisateur)
class UtilisateurAdmin(UserAdmin):
    # Champs affichés dans la liste
    list_display = [
        'username',
        'email',
        'first_name',
        'last_name',
        'age',
        'telephone',
        'is_staff',
        'is_active'
    ]
    
    # Champs pour filtrer
    list_filter = ['is_staff', 'is_active', 'is_superuser']
    
    # Champs pour la recherche
    search_fields = ['username', 'email', 'first_name', 'last_name']
    
    # Organisation des champs dans le formulaire de détail
    fieldsets = UserAdmin.fieldsets + (
        ('Informations supplémentaires', {
            'fields': ('photo_de_profile', 'description', 'age', 'lien_cv', 'telephone')
        }),
    )
    
    # Champs lors de la création d'un nouvel utilisateur
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informations supplémentaires', {
            'fields': ('photo_de_profile', 'description', 'age', 'lien_cv', 'telephone')
        }),
    )