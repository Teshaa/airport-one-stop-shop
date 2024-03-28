from .models import FoodItem, FoodOrder, FoodType, Restaurant, RestaurantImage
from rest_framework import serializers


class RestaurantImageSerializer(serializers.ModelSerializer):
    class Meta: 
        model = RestaurantImage
        fields = ("image",)

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    images = RestaurantImageSerializer(read_only=True, many=True)
    class Meta:
        model = Restaurant
        fields = ("id", "url", "name", "logo", "location", "images", "created_at", "updated_at")
        extra_kwargs= {"url": {"view_name": "meals:restaurant-detail"}}


class FoodTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FoodType
        fields = ("id", "url", "name","description", "image","created_at","updated_at")
        extra_kwargs = {"url": {"view_name": "meals:food-type-detail"}}


class FoodItemSerializer(serializers.HyperlinkedModelSerializer):
    type = FoodTypeSerializer(read_only=True)
    class Meta:
        model = FoodItem
        fields = (
            "id", "url", "restaurant", "name", "price","preparation_time", 
            "type","rating", "description",
            "readily_available","image", "created_at", "updated_at"
            )
        extra_kwargs= {
            "url": {"view_name": "meals:food-detail"}, 
            "user":{"view_name": "users:user-detail"},
            "restaurant":{"view_name": "meals:restaurant-detail"},
            "type": {"view_name": "meals:food-type-detail"}
            }
        

class FoodOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FoodOrder
        fields = (
            "id", "url", "user", "price", "status", 
          "food_item", "food_item", "status", "created_at", "updated_at"
          )
        extra_kwargs= {
            "url": {"view_name": "meals:restaurant-detail"}, 
            "user":{"view_name": "users:user-detail"},
            "food_item": {"view_name": "meals:food-detail"}
            }
        

        










