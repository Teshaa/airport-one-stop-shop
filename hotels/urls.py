from rest_framework import routers
from django.urls import path

from hotels.views import HotelViewSet, RoomViewSet, RoomTypeViewSet, ReservationViewSet

app_name = "hotel"

router = routers.DefaultRouter()
router.register(prefix="reservations", viewset=ReservationViewSet, basename="reservation")
router.register(prefix="rooms-types", viewset=RoomTypeViewSet, basename="room-type")
router.register(prefix="rooms", viewset=RoomViewSet, basename="room")
router.register(prefix="", viewset=HotelViewSet, basename="hotel")

urlpatterns = router.urls
