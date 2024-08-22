from django.shortcuts import render
from .models import *

# Create your views here.
def profil(request):
    profil = Profile.objects.get(pk=1)
    skills = Skills.objects.all()
    
    context = {
        'profile': profil,
        'skills': skills
    }
    return render(request, 'profil.html', context)