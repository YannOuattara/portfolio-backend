import logging
from rest_framework import generics, permissions, status

logger = logging.getLogger(__name__)
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from django.core.mail import send_mail
from django.conf import settings as django_settings
from django.contrib.auth import get_user_model
from .models import Localisation, Projet, Experience, Service, PriseDeContact, ReseauSocial
from .serializer import (
    LocalisationSerializer,
    ProjetSerializer,
    ExperienceSerializer,
    ServiceSerializer,
    PriseDeContactSerializer,
    ReseauSocialSerializer,
)


# ── Localisation ──────────────────────────────────────────────────────────────

@extend_schema(tags=['Localisation'])
class LocalisationListView(generics.ListAPIView):
    queryset = Localisation.objects.all()
    serializer_class = LocalisationSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Localisation'])
class LocalisationCreateView(generics.CreateAPIView):
    queryset = Localisation.objects.all()
    serializer_class = LocalisationSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Localisation'])
class LocalisationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Localisation.objects.all()
    serializer_class = LocalisationSerializer
    permission_classes = [permissions.AllowAny]


# ── Projets ───────────────────────────────────────────────────────────────────

@extend_schema(tags=['Projets'])
class ProjetListView(generics.ListAPIView):
    serializer_class = ProjetSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        qs = Projet.objects.all()
        categorie = self.request.query_params.get('categorie')
        en_vedette = self.request.query_params.get('en_vedette')
        if categorie:
            qs = qs.filter(categorie=categorie)
        if en_vedette and en_vedette.lower() == 'true':
            qs = qs.filter(en_vedette=True)
        return qs


@extend_schema(tags=['Projets'])
class ProjetCreateView(generics.CreateAPIView):
    queryset = Projet.objects.all()
    serializer_class = ProjetSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Projets'])
class ProjetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Projet.objects.all()
    serializer_class = ProjetSerializer
    permission_classes = [permissions.AllowAny]


# ── Expériences ───────────────────────────────────────────────────────────────

@extend_schema(tags=['Expériences'])
class ExperienceListView(generics.ListAPIView):
    serializer_class = ExperienceSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        qs = Experience.objects.all()
        type_exp = self.request.query_params.get('type')
        if type_exp:
            qs = qs.filter(type=type_exp)
        return qs


@extend_schema(tags=['Expériences'])
class ExperienceCreateView(generics.CreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Expériences'])
class ExperienceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [permissions.AllowAny]


# ── Services ──────────────────────────────────────────────────────────────────

@extend_schema(tags=['Services'])
class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.filter(actif=True)
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Services'])
class ServiceCreateView(generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Services'])
class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]


# ── Contacts ──────────────────────────────────────────────────────────────────

@extend_schema(tags=['Contacts'])
class PriseDeContactListView(generics.ListAPIView):
    queryset = PriseDeContact.objects.all()
    serializer_class = PriseDeContactSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Contacts'])
class PriseDeContactCreateView(generics.CreateAPIView):
    queryset = PriseDeContact.objects.all()
    serializer_class = PriseDeContactSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Capturer l'IP de l'expéditeur
        ip = (
            request.META.get('HTTP_X_FORWARDED_FOR', '').split(',')[0].strip()
            or request.META.get('REMOTE_ADDR')
        )

        # Auto-assigner le propriétaire du portfolio (premier non-superuser)
        Utilisateur = get_user_model()
        owner = Utilisateur.objects.filter(is_superuser=False).first()
        instance = serializer.save(ip_address=ip, user=owner)

        # Envoyer un email de notification au propriétaire
        destinataire = getattr(django_settings, 'CONTACT_EMAIL', None)
        if not destinataire and owner:
            destinataire = owner.email
        if destinataire and django_settings.EMAIL_HOST_PASSWORD:
            try:
                send_mail(
                    subject=f'[Portfolio] Nouveau message : {instance.sujet}',
                    message=(
                        f'Tu as reçu un nouveau message via ton portfolio.\n\n'
                        f'De : {instance.nom} <{instance.email}>\n'
                        f'Sujet : {instance.sujet}\n\n'
                        f'Message :\n{instance.message}\n\n'
                        f'---\n'
                        f'IP : {instance.ip_address}\n'
                        f'Date : {instance.date_envoi}'
                    ),
                    from_email=django_settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[destinataire],
                    fail_silently=False,
                )
            except Exception as e:
                logger.error(f'[Contact] Echec envoi email : {e}')
                print(f'[Contact] Echec envoi email : {e}')

        return Response(
            {'message': 'Message envoyé avec succès !', 'data': serializer.data},
            status=status.HTTP_201_CREATED,
        )


@extend_schema(tags=['Contacts'])
class PriseDeContactDetailView(generics.RetrieveDestroyAPIView):
    queryset = PriseDeContact.objects.all()
    serializer_class = PriseDeContactSerializer
    permission_classes = [permissions.AllowAny]


# ── Réseaux sociaux ───────────────────────────────────────────────────────────

@extend_schema(tags=['Réseaux Sociaux'])
class ReseauSocialListView(generics.ListAPIView):
    queryset = ReseauSocial.objects.filter(actif=True)
    serializer_class = ReseauSocialSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Réseaux Sociaux'])
class ReseauSocialCreateView(generics.CreateAPIView):
    queryset = ReseauSocial.objects.all()
    serializer_class = ReseauSocialSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Réseaux Sociaux'])
class ReseauSocialDetailView(generics.RetrieveDestroyAPIView):
    queryset = ReseauSocial.objects.all()
    serializer_class = ReseauSocialSerializer
    permission_classes = [permissions.AllowAny]
