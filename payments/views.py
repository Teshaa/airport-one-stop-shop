from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action

from payments.models import Payment
from payments.serilaizers import PaymentSerializer


# Create your views here.


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer





