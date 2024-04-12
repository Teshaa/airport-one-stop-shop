from core.serializers import TerminalSerializer
from users.serializers import UserSerializer
from .models import FoodItem, FoodOrder, FoodType, Restaurant, RestaurantImage
from rest_framework import serializers
from decouple import config


class RestaurantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantImage
        fields = ("image",)


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    images = RestaurantImageSerializer(read_only=True, many=True)

    class Meta:
        model = Restaurant
        fields = ("id", "url", "name", "logo",  "images", "created_at", "updated_at")
        extra_kwargs = {"url": {"view_name": "meals:restaurant-detail"}}


class FoodTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FoodType
        fields = ("id", "url", "name", "description", "image", "created_at", "updated_at")
        extra_kwargs = {"url": {"view_name": "meals:food-type-detail"}}


class FoodItemSerializer(serializers.HyperlinkedModelSerializer):
    type = FoodTypeSerializer(read_only=True)

    class Meta:
        model = FoodItem
        fields = (
            "id", "url", "restaurant", "name", "price", "preparation_time",
            "type", "rating", "description",
            "readily_available", "image", "created_at", "updated_at"
        )
        extra_kwargs = {
            "url": {"view_name": "meals:food-detail"},
            "user": {"view_name": "users:user-detail"},
            "restaurant": {"view_name": "meals:restaurant-detail"},
            "type": {"view_name": "meals:food-type-detail"}
        }

    def to_representation(self, instance):
        _dict = super().to_representation(instance)
        _dict["restaurant"] = RestaurantSerializer(instance=instance.restaurant , context=self.context).data
        
        return _dict


    


class FoodOrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = FoodOrder
        fields = (
            "id", "user", "price", "quantity", "terminal",
            "food_item", "food_item", "status", "created_at", "updated_at"
        )
        extra_kwargs = {
            "status": {"read_only": True},
            "price": {"read_only": True},
        }

    def to_representation(self, instance):
        _dict = super().to_representation(instance)
        _dict["food_item"] = FoodItemSerializer(instance=instance.food_item, context=self.context).data
        _dict["terminal"] = TerminalSerializer(instance=instance.terminal, context=self.context).data
        
        return _dict


class OrderPaymentSerializer(serializers.Serializer):
    phoneNumber = serializers.CharField(max_length=10)