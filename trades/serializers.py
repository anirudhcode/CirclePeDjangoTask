from rest_framework import serializers
from .models import Trade
from cargo.serializers import CargoSerializer
from inventory.models import Inventory
from cargo.models import Cargo

class TradeSerializer(serializers.ModelSerializer):
    cargo = CargoSerializer()

    class Meta:
        model = Trade
        fields = ['id', 'seller', 'buyer', 'status', 'amount', 'cargo', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class NewTradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = ['id', 'seller', 'buyer', 'status', 'amount', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at', 'status']

    def create(self, validated_data):
        trade = Trade.objects.create(**validated_data)
        return trade
    


class NewCargoTradeSerializer(serializers.ModelSerializer):
    cargo = CargoSerializer()
    class Meta:
        model = Trade
        fields = ['id', 'seller', 'buyer', 'status', 'cargo', 'amount', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at', 'status']

    def create(self, validated_data):
        cargo_data = validated_data.pop('cargo')
        cargo = CargoSerializer.create(CargoSerializer(), validated_data=cargo_data)
        trade = Trade.objects.create(cargo=cargo, **validated_data)
        return trade
