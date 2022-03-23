from rest_framework import serializers
from .models import Payables, Transaction
from datetime import datetime

class PayablesSerializer(serializers.ModelSerializer):
    
    #codigo_barra=serializers.CharField(max_length=255, required=True)
    tipo_servicio=serializers.CharField(max_length=25)
    descripcion_servicio=serializers.CharField(max_length=255)
    fecha_vencimiento=serializers.DateField(default=datetime.now)
    importe_servicio=serializers.FloatField()
    status_pago=serializers.CharField(max_length=25)

    class Meta:
        model = Payables
        fields = ('__all__')

class TransactionSerializer(serializers.ModelSerializer):
    
    codigo_barra=serializers.CharField(max_length=25) #PayablesSerializer(required=True) #
    metodo_pago=serializers.CharField(max_length=25)
    numero_tarjeta=serializers.CharField(max_length=20, default="")
    importe_pago=serializers.FloatField()
    fecha_pago=serializers.DateField(default=datetime.today().strftime('%Y-%m-%d'))

    class Meta:
        model = Transaction
        fields = ('__all__')
    
    def create(self, validated_data):
        id_codigo_barras=validated_data.pop('codigo_barra')
        
        payable=Payables.objects.get(codigo_barra=id_codigo_barras)
        
        validated_data["codigo_barra"]=payable

        # guardamos la transaccion
        transaction=Transaction()
        transaction.codigo_barra=validated_data["codigo_barra"]
        transaction.metodo_pago=validated_data["metodo_pago"]
        transaction.numero_tarjeta=validated_data["numero_tarjeta"]
        transaction.importe_pago=validated_data["importe_pago"]
        transaction.fecha_pago=validated_data["fecha_pago"]
        transaction.save()
        
        # si el importe es mayor o igual a la boleta, cambiamos a estado pagado
        if (transaction.importe_pago>=payable.importe_servicio):
            payable.status_pago="paid"
        else:
            payable.status_pago="partial_paid"
        payable.save()



        return transaction

