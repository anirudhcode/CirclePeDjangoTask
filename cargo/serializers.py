from rest_framework import serializers
from .models import Cargo
from inventory.models import Inventory
from spacestations.models import SpaceStations
from inventory.models import Inventory

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['id', 'productName', 'description', 'spacestation']
class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = ['id', 'description', 'item', 'weight', 'volume', 'destination', 'shipment_date', 'delivery_date']
        read_only_fields = ['id', 'shipment_date', 'delivery_date']
    
    def create(self, validated_data):
        cargo = Cargo.objects.create(**validated_data)
        return cargo
    
class RecentCargoSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    class Meta:
        model = Cargo
        fields = ['id', 'item', 'destination', 'shipment_date', 'status', 'delivery_date']