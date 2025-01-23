from django.shortcuts import redirect, render
from apps.productos.forms import FormularioProducto, FormularioMateriales
from .models import Block, Materiales
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView


def regProductos(request):
    productos = Block.objects.all()  # Obtén todos los productos de la base de datos
    return render(request, 'productos/regProductos.html', {'productos': productos})


def agregarProducto(request):
    form = FormularioProducto() 
    if request.method == 'POST':
        form = FormularioProducto(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('/productos')  
    return render(request, 'productos/agregarProducto.html', {'form': form})

class ProductoUpdateView(UpdateView):
    model = Block
    form_class = FormularioProducto
    template_name = 'productos/editarProducto.html' 
    success_url = reverse_lazy('productos:regProductos')  
    
def regMateriales(request):
    materiales = Materiales.objects.all()
    return render(request,'productos/regMateriales.html',{'materiales': materiales})



def agregarMateriales(request):
    form = FormularioMateriales() 
    if request.method == 'POST':
        form = FormularioMateriales(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('/productos/regMateriales')  
    return render(request, 'productos/agregarMateriales.html', {'form': form})


class MaterialesUpdateView(UpdateView):
    model = Materiales
    form_class = FormularioMateriales
    template_name = 'productos/editarMateriales.html' 
    success_url = reverse_lazy('productos:regMateriales')  