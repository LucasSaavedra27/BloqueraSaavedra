from django import forms
from .models import Empleado

class FormularioEmpleado(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = [
            'nombre', 
            'direccion', 
            'telefono', 
            'estado',  
        ]
        labels = {
            'nombre': 'Nombre',
            'direccion': 'Dirección',
            'telefono': 'Número de teléfono',
            'estado': 'Estado del empleado',
        }
        ESTADO_CHOICES = [
            ('activo', 'Activo'),
            ('inactivo', 'Inactivo'),
        ]   
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }