from rest_framework import serializers

from core.models import Terminal, Service


class TerminalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terminal
        fields = ("name", "created_at", "updated_at")


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ("title", 'image', "created_at", "updated_at")

