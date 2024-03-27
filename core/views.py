from django.shortcuts import render
from rest_framework import viewsets

from core.models import Service, Terminal
from core.serializers import ServiceSerializer, TerminalSerializer
# Create your views here.


class TerminalViewSet(viewsets.ModelViewSet):
    serializer_class = TerminalSerializer
    queryset = Terminal.objects.all()

class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()