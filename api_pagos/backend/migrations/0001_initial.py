# Generated by Django 4.0.3 on 2022-03-23 00:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payables',
            fields=[
                ('codigo_barra', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('tipo_servicio', models.CharField(max_length=25)),
                ('descripcion_servicio', models.CharField(max_length=255)),
                ('fecha_vencimiento', models.DateField(default=datetime.datetime.now)),
                ('importe_servicio', models.FloatField()),
                ('status_pago', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metodo_pago', models.CharField(choices=[('1', 'Debit Card'), ('2', 'Credit Card'), ('3', 'Cash')], default='3', max_length=25)),
                ('numero_tarjeta', models.CharField(max_length=20)),
                ('importe_pago', models.FloatField()),
                ('fecha_pago', models.DateField(default=datetime.datetime.now)),
                ('codigo_barra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.payables')),
            ],
        ),
    ]
