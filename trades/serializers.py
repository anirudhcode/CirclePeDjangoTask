from rest_framework import serializers
from .models import Trade
from cargo.serializers import CargoSerializer
from inventory.models import Inventory

class TradeSerializer(serializers.ModelSerializer):
    cargo = CargoSerializer()

    class Meta:
        model = Trade
        fields = ['id', 'seller', 'buyer', 'status', 'amount', 'cargo', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class NewTradeSerializer(serializers.ModelSerializer):
    cargo = CargoSerializer(required=False, allow_null=True)

    class Meta:
        model = Trade
        fields = ['id', 'seller', 'buyer', 'status', 'amount', 'cargo', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def create(self, validated_data):
        trade = Trade.objects.create(**validated_data)
        cargo_data = validated_data.pop('cargo', None)

        if cargo_data:
            cargo_serializer = CargoSerializer(data=cargo_data)
            cargo_serializer.is_valid(raise_exception=True)
            cargo = cargo_serializer.save()
            trade.cargo = cargo
            volume = cargo.volume
            inventory = Inventory.objects.get(id=cargo.item.id)
            inventory.volume -= volume
            inventory.save()
            trade.save()


        return trade
    
    def update(self, instance, validated_data):
        cargo_data = validated_data.pop('cargo', None)
        if cargo_data:
            if instance.cargo:
                volume = instance.cargo.volume
                cargo_serializer = CargoSerializer(instance.cargo, data=cargo_data, partial=True)
                cargo_serializer.is_valid(raise_exception=True)
                cargo_serializer.save()
                newVolume = cargo_serializer.instance.volume
                inventory = Inventory.objects.get(id=cargo_data['item'])
                inventory.volume += volume
                inventory.volume -= newVolume
                inventory.save()
            else:
                cargo_serializer = CargoSerializer(data=cargo_data)
                cargo_serializer.is_valid(raise_exception=True)
                cargo = cargo_serializer.save()
                instance.cargo = cargo
                volume = cargo.volume
                inventory = Inventory.objects.get(id=cargo.item.id)
                inventory.volume -= volume
                inventory.save()
        instance.save()
        return instance
