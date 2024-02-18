from rest_framework import serializers

from hotels.models import Hotel, Room, RoomType, Reservation


class HotelImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hotel

class HotelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hotel
        fields = (
            "id", "url", "name", "address", "email", "phoneNumber", "rating",
            "amenities", "description", "created_at",
            "updated_at"
        )
        extra_kwargs = {
            "url": {"view_name": "hotel:hotel-detail"}
        }


class RoomTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RoomType
        fields = (
            "id", "url", "name", "description", "created_at", "updated_at")
        extra_kwargs = {
            "url": {"view_name": "hotel:room-type-detail"}
        }


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    hotel = HotelSerializer()
    type = RoomTypeSerializer()

    class Meta:
        model = Room
        fields = [
            "id", "url", "number", "description", "type", "hotel", "capacity", "price_per_night", "available",
            "feature",
            "created_at", "updated_at"]
        extra_kwargs = {
            "url": {"view_name": "hotel:room-detail"},
            # "type": {"view_name": "hotel:room-type-detail"},
            # "hotel": {"view_name": "hotel:hotel-detail"}
        }


class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reservation
        fields = [
            "id", "user", "room", "checkin_date", "checkout_date", "status", "created_at", "updated_at"]

        extra_kwargs = {
            "url": {"view_name": "hotel:reservation-detail"},
            "user": {"view_name": "users:user-detail"},
            "room": {"view_name": "hotel:room-detail"},
        }
