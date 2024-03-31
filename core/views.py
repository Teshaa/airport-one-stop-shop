from django.shortcuts import render
from rest_framework import viewsets, views
from rest_framework.response import Response
from urllib import parse
from core.models import Service, Terminal
from core.serializers import ServiceSerializer, TerminalSerializer, OrderSerializer
from hotels.models import Reservation, Room


# Create your views here.


class TerminalViewSet(viewsets.ModelViewSet):
    serializer_class = TerminalSerializer
    queryset = Terminal.objects.all()


class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

