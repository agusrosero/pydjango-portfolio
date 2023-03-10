from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField


# Creamos nuestro modelo de datos
class Proyect(models.Model):
    titulo = CharField(max_length=100)
    descripcion = CharField(max_length=250)
    image = ImageField(upload_to="portfolio/image")
    url = URLField(blank=True)
