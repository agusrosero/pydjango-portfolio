from django.urls import path
from . import views


urlpatterns = [
    path('text_to_html/', views.convertor_view, name='convertor_view'),
]