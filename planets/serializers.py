from rest_framework import serializers
from .models import Planets

class PlanetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planets
        fields = ['id', 'localName', 'englishName', 'location', 'planetAttributes', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
        