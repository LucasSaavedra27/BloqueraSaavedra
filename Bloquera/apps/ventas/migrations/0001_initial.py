# Generated by Django 5.1.5 on 2025-01-28 16:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaDeVenta', models.DateField()),
                ('formaDePago', models.CharField(choices=[('Efectivo', 'Efectivo'), ('Transferencia', 'Transferencia'), ('Débito', 'Débito'), ('Crédito', 'Crédito')], max_length=15)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('lugarVenta', models.CharField(default='Capital', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('subTotal', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('block', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='detalleBlock', to='productos.block')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalleVenta', to='ventas.venta')),
            ],
        ),
    ]
