from rest_framework import serializers
from .models import Cargo

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = ['id', 'description','item', 'weight', 'volume', 'origin', 'destination', 'shipment_date', 'delivery_date']
        read_only_fields = ['id', 'shipment_date', 'delivery_date']
