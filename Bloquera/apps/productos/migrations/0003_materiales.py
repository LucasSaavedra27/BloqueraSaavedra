# Generated by Django 5.1.5 on 2025-01-23 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_alter_block_cantidaddisponible'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materiales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('unidadDeMedida', models.CharField(choices=[('Kg', 'Kilogramos'), ('g', 'Gramos'), ('palet', 'Palet'), ('l', 'Litros'), ('m3', 'Metro cúbico'), ('bolsa', 'Bolsa'), ('u', 'Unidad')], max_length=15)),
                ('precioDeCosto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidadDisponible', models.PositiveIntegerField()),
                ('cantidadMinRequerida', models.PositiveIntegerField()),
            ],
        ),
    ]
