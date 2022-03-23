from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PayablesSerializer, TransactionSerializer
from .models import Payables, Transaction


class PayablesViews(APIView):
    def get(self, request, status="pending"):
        payables=Payables.objects.filter(status_pago=status)
        serializer=PayablesSerializer(payables, many=True)
        return Response(serializer.data, 200)

    def post(self, request):
        try:
            serializer = PayablesSerializer(data=request.data)
            if (serializer.is_valid()):
                serializer.save()
                return Response({"status":"ok", "data":serializer.data}, 200)
            else:
                return Response({"status":"error", "data":serializer.errors}, 400)
        except Exception as e:
            return Response({"status":"error", "data":str(e)}, 500)


class TransactionViews(APIView):
    def get(self, request, start_date=None, end_date=None):

        if (start_date and end_date):
            transactions=Transaction.objects.filter(fecha_pago__gte=start_date, fecha_pago__lte=end_date)
        else:
            transactions=Transaction.objects.all()
        serializer=TransactionSerializer(transactions, many=True)
        return Response(serializer.data, 200)


    def post(self, request):
        try:
            serializer = TransactionSerializer(data=request.data)
            
            if (serializer.is_valid()):
                serializer.save()
                return Response({"status":"ok", "data":serializer.data}, 200)
            else:
                return Response({"status":"error", "data":serializer.errors}, 400)
        except Exception as e:
            return Response({"status":"error", "data":str(e)}, 500)
    
    
