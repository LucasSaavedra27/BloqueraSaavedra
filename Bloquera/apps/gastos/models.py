from django.db import models
from apps.productos.models import Materiales
from apps.personal.models import Proveedor, Empleado

class Gasto(models.Model):
    TIPO_GASTO = [
        ('Material', 'Compra de Material'),
        ('Salario', 'Pago de Salario'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_GASTO, null=False,blank=False)
    fecha = models.DateField(null=False,blank=False)
    monto = models.DecimalField(max_digits=10, decimal_places=2,null=False,blank=False)
    FORMA_PAGO = [
        ('Efectivo','Efectivo'),
        ('Transferencia','Transferencia'),
        ('Débito','Débito'),
        ('Crédito','Crédito'),
    ]
    formaDePago = models.CharField(max_length=15, choices=FORMA_PAGO,blank=False, null=False)
    
    class Meta:
        abstract = True

class GastoMaterial(Gasto):
    proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE,related_name='gastoProveedor')
    
    def __str__(self):
        return f"Tipo: {self.tipo} - monto: {self.monto}"

class GastoSalario(Gasto):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE,related_name='gastoSalario')

    def __str__(self):
        return f"Salario para: {self.empleado.nombre} : ${self.monto}"


class DetallesGastosMateriales(models.Model):
    materiales = models.ForeignKey(Materiales,on_delete=models.CASCADE,related_name='detalleMateriales')
    gasto = models.ForeignKey(GastoMaterial,on_delete=models.CASCADE,related_name='detalleGastoMaterial')
    cantidad = models.PositiveIntegerField(blank=False, null=False)
    subTotal = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    
    def save(self, *args, **kwargs):
        self.subTotal = self.cantidad * self.materiales.precioDeCosto
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.materiales.nombre} {self.cantidad} {self.subTotal}"