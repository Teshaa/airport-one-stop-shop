from rest_framework import serializers
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)
from hotels.models import Hotel, HotelImage, Room, RoomImage, RoomType, Reservation
from taggit.models import Tag

from users.serializers import UserSerializer


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


class NestedRoomSerializer(TaggitSerializer, serializers.HyperlinkedModelSerializer):
    type = RoomTypeSerializer()
    images = RoomImageSerializer(read_only=True, many=True)
    feature = TagListSerializerField()

    class Meta:
        model = Room
        fields = [
            "id", "url", "number", "description", "type", "capacity", "price_per_night", "available",
            "feature", "images",
            "created_at", "updated_at"
            ]
        extra_kwargs = {
            "url": {"view_name": "hotel:room-detail"},
            "type": {"view_name": "hotel:room-type-detail"},
            # "hotel": {"view_name": "hotel:hotel-detail"}
        }


class HotelSerializer(TaggitSerializer, serializers.HyperlinkedModelSerializer):
    images = HotelImageSerializer(read_only=True, many=True)
    rooms = NestedRoomSerializer(read_only=True, many=True)
    amenities = TagListSerializerField()

    class Meta:
        model = Hotel
        fields = (
            "id", "url", "name", "logo", "longitude", "latitude", "address", "email", "phoneNumber", "rating",
            "amenities", "description", "images", "rooms", "created_at",
            "updated_at"
        )
        extra_kwargs = {
            "url": {"view_name": "hotel:hotel-detail"},
            "rooms": {"view_name": "hotel:room-detail"}
        }


class ReservationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Reservation
        fields = [
            "id", "user", "room", "checkin_date", "nights", "price_per_night", "status", "created_at", "updated_at"]

        extra_kwargs = {
            # "url": {"view_name": "hotel:reservation-detail"},
            # "room": {"view_name": "hotel:room-detail"},
            "status": {"read_only": True},
            "price_per_night": {"read_only": True},
        }

    def to_representation(self, instance):
        _dict = super().to_representation(instance)
        _dict["room"] = RoomSerializer(instance=instance.room, context=self.context).data
        return _dict


class RoomSerializer(TaggitSerializer, serializers.HyperlinkedModelSerializer):
    hotel = HotelSerializer()
    type = RoomTypeSerializer()
    images = RoomImageSerializer(read_only=True, many=True)
    feature = TagListSerializerField()

    class Meta:
        model = Room
        fields = [
            "id", "url", "number", "description", "type", "rating",
            "hotel", "capacity", "price_per_night", "available",
            "feature", "images", "created_at", "updated_at"
        ]
        extra_kwargs = {
            "url": {"view_name": "hotel:room-detail"},
            # "type": {"view_name": "hotel:room-type-detail"},
            # "hotel": {"view_name": "hotel:hotel-detail"}
        }


class TagSerializer(TaggitSerializer, serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']
