from django.shortcuts import render
from .models import Proyect


def home(request):
    try:
        projects = Proyect.objects.all()
    except Proyect.DoesNotExist:
        projects = []
    
    return render(request, "home.html", {"projects": projects})
