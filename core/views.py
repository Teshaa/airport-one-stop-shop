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


class OrderView(views.APIView):
    def post(self, request):
        print(request.data)
        # serializer = OrderSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        print(request.user)
        for item in request.data["items"]:
            id = parse.urlparse(item["product"]).path.split("/")[-2]
            if item["productType"] == "accomodation":
                Reservation.objects.create(user=request.user, room=Room.objects.get(id=id) )
            elif item["productType"] == "meal":
                pass
            print(id, item)
        return Response({"success": True})
