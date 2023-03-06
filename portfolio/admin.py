from django.contrib import admin
from .models import Proyect

"""
Registramos la clase Proyect (haciendo que se muestre el titulo, descripcion,
image, url - como ya definimos en models.py - mediante el ingreso a www.localhost:8000.com/admin)
"""
admin.site.register(Proyect)
