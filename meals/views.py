from django.shortcuts import render
from rest_framework import viewsets, response
from rest_framework.decorators import action
from meals.filters import ProductFilter
from meals.models import FoodItem, FoodOrder, FoodType, Restaurant
from meals.serializers import FoodItemSerializer, FoodOrderSerializer, FoodTypeSerializer, OrderPaymentSerializer, RestaurantSerializer
from django_daraja.mpesa.core import MpesaClient

from payments.models import Payment

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
    filterset_class = ProductFilter
    search_fields = ["name", "description", "restaurant__name"]



class FoodOrderViewSet(viewsets.ModelViewSet):
    serializer_class = FoodOrderSerializer
    queryset = FoodOrder.objects.all()

    def perform_create(self, serializer):
        serializer.validated_data["user"] = self.request.user
        serializer.validated_data["price"] = serializer.validated_data["food_item"].price
        super().perform_create(serializer)


    @action(detail=True, methods=["POST"], serializer_class=OrderPaymentSerializer)
    def make_payment(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = self.get_object()
        total_price = order.price * order.quantity
        client = MpesaClient()
        _response = client.stk_push(
            serializer.validated_data["phoneNumber"], 
            int(total_price), 
            "Airport on stop shop", 
            "Payment for meals ordered", 
            "https://api.darajambili.com/express-payment",
            )
        if _response.status_code == 200:
            data = _response.json()
            merchantId = data["MerchantRequestID"]
            checkoutId = data["CheckoutRequestID"]
            desc = data["ResponseDescription"]
            message = data["CustomerMessage"]
            code = data["ResponseCode"]
            order.status = "delivered"
            order.save()
            Payment.objects.create(
                food_order=order,
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



"""
{
    'MerchantRequestID': '53e3-4aa8-9fe0-8fb5e4092cdd1930931', 
    'CheckoutRequestID': 'ws_CO_19042024174056772793889658', 
    'ResponseCode': '0', 
    'ResponseDescription': 'Success. Request accepted for processing', 
    'CustomerMessage': 'Success. Request accepted for processing'
}
"""