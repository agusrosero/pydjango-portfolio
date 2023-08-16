from django.shortcuts import render
from .models import Proyect


def home(request):
    proyects = Proyect.objects.all()
    return render(request, "home.html", {"proyects": proyects})
