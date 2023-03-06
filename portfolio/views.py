from django.shortcuts import render
from .models import Proyect


# Definimos que hara cuando llegue a una url.
# Render accede a cualquier carpeta llamada templates.
def home(request):
    # Trae todos los proyectos que estan en obyect:
    proyects = Proyect.objects.all()
    return render(request, "home.html", {"proyects": proyects})
