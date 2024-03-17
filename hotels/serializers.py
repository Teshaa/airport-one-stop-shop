from rest_framework import serializers

from hotels.models import Hotel, HotelImage, Room, RoomImage, RoomType, Reservation  


class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ("id", "image")

class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ("id", "image")


class RoomTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RoomType
        fields = (
            "id", "url", "name", "description", "created_at", "updated_at",
            )
        extra_kwargs = {
            "url": {"view_name": "hotel:room-type-detail"}
        }



class NestedRoomSerializer(serializers.HyperlinkedModelSerializer):
    type = RoomTypeSerializer()
    images = RoomImageSerializer(read_only=True, many=True)

    class Meta:
        model = Room
        fields = [
            "id", "url", "number", "description", "type", "capacity", "price_per_night", "available",
            "feature", "images",
            "created_at", "updated_at"]
        extra_kwargs = {
            "url": {"view_name": "hotel:room-detail"},
            "type": {"view_name": "hotel:room-type-detail"},
            # "hotel": {"view_name": "hotel:hotel-detail"}
        }




class HotelSerializer(serializers.HyperlinkedModelSerializer):
    images = HotelImageSerializer(read_only=True, many=True)
    rooms = NestedRoomSerializer(read_only=True, many=True)
    class Meta:
        model = Hotel
        fields = (
            "id", "url", "name", "address", "email", "phoneNumber", "rating",
            "amenities", "description", "images","rooms", "created_at",
            "updated_at"
        )
        extra_kwargs = {
            "url": {"view_name": "hotel:hotel-detail"},
            "rooms": {"view_name": "hotel:room-detail"}
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


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    hotel = HotelSerializer()
    type = RoomTypeSerializer()
    images = RoomImageSerializer(read_only=True, many=True)


    class Meta:
        model = Room
        fields = [
            "id", "url", "number", "description", "type",
            "hotel", "capacity", "price_per_night", "available",
            "feature", "images", "created_at", "updated_at"
            ]
        extra_kwargs = {
            "url": {"view_name": "hotel:room-detail"},
            # "type": {"view_name": "hotel:room-type-detail"},
            # "hotel": {"view_name": "hotel:hotel-detail"}
        }

