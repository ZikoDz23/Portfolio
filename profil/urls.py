from django.urls import path, include
from . import views
from .views import profil

urlpatterns = [
    path('', views.profil, name='profil')
]
