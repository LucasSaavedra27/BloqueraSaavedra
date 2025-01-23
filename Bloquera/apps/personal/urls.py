from django.urls import path
from . import views
from .views import EmpleadoUpdateView

app_name = 'personal'

urlpatterns = [
    path('regEmpleados/', views.regEmpleados, name='regEmpleados'),  # Ajusta esto según tus vistas
    path('agregarEmpleado/', views.agregarEmpleado, name='agregarEmpleado'),
    path('editarEmpleado/<int:pk>/', EmpleadoUpdateView.as_view(), name='editarEmpleado'),# Ajusta esto según tus vistas
]
