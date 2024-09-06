from rest_framework import serializers
from .models import Planets

class PlanetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planets
        fields = ['id', 'localName', 'englishName', 'location', 'planetAttributes', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
        
class PlanetSummarySerializer(serializers.ModelSerializer):
    spaceStations = serializers.SerializerMethodField()
    class Meta:
        model = Planets
        fields = ['localName', 'englishName', 'location', 'planetAttributes', 'spaceStations', 'created_at']
        
    def get_spaceStations(self, instance):
        return instance.spacestations.count()