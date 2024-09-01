from django.db import models
import uuid 
from planets.models import Planets

class SpaceStations(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    planet = models.ForeignKey(Planets, on_delete=models.CASCADE, related_name='spacestations')
    capacity = models.IntegerField()
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # def __str__(self):