from django.shortcuts import redirect, render
from .models import Empleado
from .forms import FormularioEmpleado
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

def regEmpleados(request):
    empleados = Empleado.objects.all() 
    return render(request, 'personal/regEmpleados.html', {'empleados': empleados})

def agregarEmpleado(request):
    form = FormularioEmpleado() 
    if request.method == 'POST':
        form = FormularioEmpleado(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('/personal/regEmpleados')  
    return render(request, 'personal/agregarEmpleados.html', {'form': form})

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    form_class = FormularioEmpleado
    template_name = 'personal/editarEmpleados.html' 
    success_url = reverse_lazy('personal:regEmpleados')  