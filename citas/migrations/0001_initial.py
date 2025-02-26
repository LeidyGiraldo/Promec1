# Generated by Django 5.0.4 on 2024-05-13 15:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_servicio', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
                'db_table': 'servicio',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_persona', models.CharField(max_length=50, verbose_name='Nombre')),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('telefono', models.IntegerField(verbose_name='Telefono')),
                ('fecha_cita', models.DateField(verbose_name='Fecha')),
                ('hora_cita', models.TimeField(verbose_name='Hora')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citas.servicio')),
            ],
            options={
                'verbose_name': 'Cita',
                'verbose_name_plural': 'Citas',
                'db_table': 'citas',
                'ordering': ['id'],
            },
        ),
    ]
