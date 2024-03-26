from .models import FoodItem, FoodOrder, FoodType, OrderItem, Restaurant, RestaurantImage
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
            "type","rating",
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
            "id", "url", "user", "restaurant", "total_price",
          "order_time", "order_time", "status", "created_at", "updated_at"
          )
        extra_kwargs= {
            "url": {"view_name": "meals:restaurant-detail"}, 
            "user":{"view_name": "users:user-detail"},
            "restaurant":{"view_name": "meals:restaurant-detail"}
            }
        


class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FoodItem
        fields = ("id", "url",  "order", "food_item", "quantity",)
        extra_kwargs= {
            "url": {"view_name": "meals:items-detail"},  
            "order":{"view_name": "users:order-detail"},
            "food_item":{"view_name": "meals:food-detail"}
            }
        










