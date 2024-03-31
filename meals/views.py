from django.shortcuts import render
from rest_framework import viewsets

from meals.models import FoodItem, FoodOrder, FoodType, Restaurant
from meals.serializers import FoodItemSerializer, FoodOrderSerializer, FoodTypeSerializer, RestaurantSerializer


# Create your views here.


class RestaurantViewSet(viewsets.ModelViewSet):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()


class FoodTypeViewSet(viewsets.ModelViewSet):
    serializer_class = FoodTypeSerializer
    queryset = FoodType.objects.all()


class FoodItemViewSet(viewsets.ModelViewSet):
    serializer_class = FoodItemSerializer
    queryset = FoodItem.objects.all()


class FoodOrderViewSet(viewsets.ModelViewSet):
    serializer_class = FoodOrderSerializer
    queryset = FoodOrder.objects.all()

    def perform_create(self, serializer):
        serializer.validated_data["user"] = self.request.user
        serializer.validated_data["price"] = serializer.validated_data["food_item"].price
        super().perform_create(serializer)
