from django.urls import path
from .views import UtilisateurListView, UtilisateurCreateView, UtilisateurDetailView, utilisateur_complet, profil_principal

urlpatterns = [
    # 1. Profil principal du portfolio (premier non-superuser)
    path('profil/', profil_principal, name='utilisateur-profil'),
    # 2. Liste de tous les utilisateurs
    path('', UtilisateurListView.as_view(), name='utilisateur-list'),
    # 3. Créer un utilisateur
    path('create/', UtilisateurCreateView.as_view(), name='utilisateur-create'),
    # 4. Détail / modifier / supprimer un utilisateur
    path('<int:pk>/', UtilisateurDetailView.as_view(), name='utilisateur-detail'),
    # 5. Profil complet avec toutes les relations imbriquées
    path('<int:pk>/complet/', utilisateur_complet, name='utilisateur-complet'),
]
