from django.db import models
import uuid
from spacestations.models import SpaceStations
class Inventory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    spacestation = models.ForeignKey(SpaceStations, on_delete=models.CASCADE, related_name='inventory')
    productName = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name