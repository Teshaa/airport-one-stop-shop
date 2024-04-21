from django.db.models import OuterRef, Subquery
from django.shortcuts import render
from rest_framework import viewsets
from taggit.models import Tag
from django_daraja.mpesa.core import MpesaClient
from hotels.filters import AccomodationFilter
from hotels.models import Hotel, Room, RoomType, Reservation
from hotels.serializers import HotelSerializer, RoomSerializer, RoomTypeSerializer, ReservationSerializer, TagSerializer
from meals.serializers import OrderPaymentSerializer
from payments.models import Payment
from rest_framework.decorators import action
from rest_framework import viewsets, response



# Create your views here.
class HotelViewSet(viewsets.ModelViewSet):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()


# Create your views here.
class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    filterset_class = AccomodationFilter
    search_fields = ["number", "description", "hotel__name"]


    # queryset = Room.objects.filter(available=True, reservations__not__in=Reservation.object.filter())
    def get_queryset(self):
        # Get the IDs of rooms that have an active reservation
        active_reservation_ids = Reservation.objects.filter(
            room=OuterRef("pk"),
            status__in=["confirmed", "checked-in"]
        ).values("room")
        # Get rooms that do not have an active reservation
        rooms_without_active_reservation = Room.objects.exclude(
            id__in=Subquery(active_reservation_ids)
        )
        return rooms_without_active_reservation


# Create your views here.
class RoomTypeViewSet(viewsets.ModelViewSet):
    serializer_class = RoomTypeSerializer
    queryset = RoomType.objects.all()  # Create your views here.


class ReservationViewSet(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()

    def perform_create(self, serializer):
        serializer.validated_data["user"] = self.request.user
        serializer.validated_data["price_per_night"] = serializer.validated_data["room"].price_per_night
        return super().perform_create(serializer)
    
    @action(detail=True, methods=["POST"], serializer_class=OrderPaymentSerializer)
    def make_payment(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        reservation = self.get_object()
        total_price = reservation.price_per_night * reservation.nights
        client = MpesaClient()
        _response = client.stk_push(
            serializer.validated_data["phoneNumber"], 
            int(total_price), 
            "Airport on stop shop", 
            "Payment for hotel reservation", 
            "https://api.darajambili.com/express-payment",
            )
        if _response.status_code == 200:
            data = _response.json()
            merchantId = data["MerchantRequestID"]
            checkoutId = data["CheckoutRequestID"]
            desc = data["ResponseDescription"]
            message = data["CustomerMessage"]
            code = data["ResponseCode"]
            reservation.status = "checked-in"
            reservation.save()
            Payment.objects.create(
                reservation=reservation,
                merchant_request_id=merchantId,
                checkout_request_id=checkoutId,
                result_code=code,
                result_description=desc,
                ammount=total_price,
                phone_number=serializer.validated_data["phoneNumber"],
                
            )
            return response.Response(data)
        else:
            return response.Response({"code": _response.status_code, "message": _response.json()})



class TagsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
