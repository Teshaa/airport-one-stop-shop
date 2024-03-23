from django.shortcuts import render
from rest_framework import viewsets

from meals.models import FoodItem, FoodOrder, FoodType, OrderItem, Restaurant
from meals.serializers import FoodItemSerializer, FoodOrderSerializer, FoodTypeSerializer, OrderItemSerializer, RestaurantSerializer
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

class OrderItemViewset(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()

