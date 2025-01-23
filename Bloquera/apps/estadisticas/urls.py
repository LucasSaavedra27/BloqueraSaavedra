from django.urls import path
from . import views

app_name = 'estadisticas'

urlpatterns = [
    path('', views.index, name='index'),  # Ajusta esto según tus vistas
    # Agrega más rutas aquí
]
