# Generated by Django 5.1.5 on 2025-01-20 14:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cedula', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('codigo', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('numero', models.CharField(max_length=10)),
                ('tipo', models.CharField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ingreso', models.DateField()),
                ('fecha_salida', models.DateField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='reservas.cliente')),
                ('codigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.habitacion')),
            ],
        ),
    ]
