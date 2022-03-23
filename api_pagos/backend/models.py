from django.db import models
from datetime import datetime

class Payables(models.Model):
    class EstadoPago(models.TextChoices):
        pending="pending","Pendiente"
        paid="paid","Pagado"
        partial_paid="partial_paid","Pago parcial"
    codigo_barra=models.AutoField(primary_key=True)
    tipo_servicio=models.CharField(max_length=25)
    descripcion_servicio=models.CharField(max_length=255)
    fecha_vencimiento=models.DateField(default=datetime.now)
    importe_servicio=models.FloatField()
    status_pago=models.CharField(max_length=25, choices=EstadoPago.choices, default=EstadoPago.pending)

class Transaction(models.Model):
    class MetodoPago(models.TextChoices):
        debit_card=1,"Debit Card"
        credit_card=2,"Credit Card"
        cash=3,"Cash"

    codigo_barra=models.ForeignKey(Payables, on_delete=models.CASCADE)
    metodo_pago=models.CharField(max_length=25, choices=MetodoPago.choices, default=MetodoPago.cash)
    numero_tarjeta=models.CharField(max_length=20)
    importe_pago=models.FloatField()
    fecha_pago=models.DateField(default=datetime.now)
