from django.contrib import admin
from .models import Post

# registramos para porder añadir publicaciones
admin.site.register(Post)
