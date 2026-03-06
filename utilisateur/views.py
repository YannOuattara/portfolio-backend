from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from drf_spectacular.utils import extend_schema
from .models import Utilisateur
from .serializer import UtilisateurSerializer, UtilisateurDetailSerializer


@extend_schema(tags=['Utilisateur'])
class UtilisateurListView(generics.ListAPIView):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Utilisateur'])
class UtilisateurCreateView(generics.CreateAPIView):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Utilisateur'])
class UtilisateurDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Utilisateur'], responses=UtilisateurDetailSerializer)
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def utilisateur_complet(request, pk):
    """Retourne le profil complet d'un utilisateur avec toutes ses relations."""
    try:
        utilisateur = Utilisateur.objects.get(pk=pk)
    except Utilisateur.DoesNotExist:
        raise NotFound(detail="Utilisateur introuvable.")
    serializer = UtilisateurDetailSerializer(utilisateur, context={'request': request})
    return Response(serializer.data)


@extend_schema(tags=['Utilisateur'], responses=UtilisateurDetailSerializer)
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def profil_principal(request):
    """Retourne le profil complet du premier utilisateur non-superuser (portfolio owner)."""
    utilisateur = Utilisateur.objects.filter(is_superuser=False).first()
    if not utilisateur:
        raise NotFound(detail="Aucun profil trouvé.")
    serializer = UtilisateurDetailSerializer(utilisateur, context={'request': request})
    return Response(serializer.data)
