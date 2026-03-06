"""
URL configuration for portfolioAngularBackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import (
    ProjetListView,
    ProjetCreateView,
    ProjetDetailView,
    ExperienceListView,
    ExperienceCreateView,
    ExperienceDetailView,
    ServiceListView,
    ServiceCreateView,
    ServiceDetailView,
    PriseDeContactListView,
    PriseDeContactCreateView,
    PriseDeContactDetailView,
    ReseauSocialListView,
    ReseauSocialCreateView,
    ReseauSocialDetailView,
    LocalisationListView,
    LocalisationCreateView,
    LocalisationDetailView,
)

urlpatterns = [
    # Projet URLs
    path('projets/', ProjetListView.as_view(), name='projet-list'),
    path('projets/create/', ProjetCreateView.as_view(), name='projet-create'),
    path('projets/<int:pk>/', ProjetDetailView.as_view(), name='projet-detail'),
    
    # Experience URLs
    path('experiences/', ExperienceListView.as_view(), name='experience-list'),
    path('experiences/create/', ExperienceCreateView.as_view(), name='experience-create'),
    path('experiences/<int:pk>/', ExperienceDetailView.as_view(), name='experience-detail'),
    
    # Service URLs
    path('services/', ServiceListView.as_view(), name='service-list'),
    path('services/create/', ServiceCreateView.as_view(), name='service-create'),
    path('services/<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),
    
    # PriseDeContact URLs
    path('contacts/', PriseDeContactListView.as_view(), name='contact-list'),
    path('contacts/create/', PriseDeContactCreateView.as_view(), name='contact-create'),
    path('contacts/<int:pk>/', PriseDeContactDetailView.as_view(), name='contact-detail'),
    
    # ReseauSocial URLs
    path('reseaux-sociaux/', ReseauSocialListView.as_view(), name='reseausocial-list'),
    path('reseaux-sociaux/create/', ReseauSocialCreateView.as_view(), name='reseausocial-create'),
    path('reseaux-sociaux/<int:pk>/', ReseauSocialDetailView.as_view(), name='reseausocial-detail'),
    
    # Localisation URLs
    path('localisations/', LocalisationListView.as_view(), name='localisation-list'),
    path('localisations/create/', LocalisationCreateView.as_view(), name='localisation-create'),
    path('localisations/<int:pk>/', LocalisationDetailView.as_view(), name='localisation-detail'),
]
