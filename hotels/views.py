from django.shortcuts import render
from rest_framework import viewsets
from taggit.models import Tag


from hotels.models import Hotel, Room, RoomType, Reservation
from hotels.serializers import HotelSerializer, RoomSerializer, RoomTypeSerializer, ReservationSerializer, TagSerializer


# Create your views here.
class HotelViewSet(viewsets.ModelViewSet):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()


# Create your views here.
class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


# Create your views here.
class RoomTypeViewSet(viewsets.ModelViewSet):
    serializer_class = RoomTypeSerializer
    queryset = RoomType.objects.all()  # Create your views here.


class ReservationViewSet(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()


class TagsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer