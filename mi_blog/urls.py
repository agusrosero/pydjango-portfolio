from django.urls import path
from .views import render_posts, post_detail

# Creamos una variable para referenciar la variable urlpatterns de abajo
app_name = "mi_blog"

urlpatterns = [
    path("", render_posts, name="posts"),
    path("<int:post_id>", post_detail, name="post_detail"),
]
