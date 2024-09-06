from rest_framework import serializers
from .models import SpaceStations

class SpaceStationsSerializer(serializers.ModelSerializer):
    planetName = serializers.SerializerMethodField()
    class Meta:
        model = SpaceStations
        fields = ['id', 'name', 'planetName', 'status']

    def get_planetName(self, obj):
        return obj.planet.localName

