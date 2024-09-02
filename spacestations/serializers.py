from rest_framework import serializers
from .models import SpaceStations

class SpaceStationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpaceStations
        fields = '__all__'

