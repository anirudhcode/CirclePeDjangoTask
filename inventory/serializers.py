from rest_framework import serializers
from .models import Inventory

class InventorySummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['id', 'productName', 'description', 'quantity']
        read_only_fields = ['id']

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['id', 'spacestation', 'productName', 'description', 'quantity']
        read_only_fields = ['id']