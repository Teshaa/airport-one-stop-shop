from rest_framework import serializers

from core.models import Terminal, Service


class TerminalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terminal
        fields = ("id", "name", "created_at", "updated_at")


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ("id", "title", 'image', "created_at", "updated_at")


class OrderItemSerializer(serializers.Serializer):
    product = serializers.URLField(required=True)
    quantity = serializers.IntegerField(required=True),
    productType = serializers.CharField(required=True)


class OrderSerializer(serializers.Serializer):
    items = OrderItemSerializer(many=True)
