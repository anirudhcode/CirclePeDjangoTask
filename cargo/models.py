from django.db import models
import uuid
from spacestations.models import SpaceStations

STATUS_CHOICES = [
    ('PENDING', 'PENDING'),
    ('IN_TRANSIT', 'IN_TRANSIT'),
    ('DELIVERED', 'DELIVERED'),
]
class Cargo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=255)
    item = models.ForeignKey('inventory.Inventory', on_delete=models.CASCADE, related_name='cargo')
    weight = models.FloatField()
    volume = models.FloatField()
    origin = models.ForeignKey(SpaceStations, on_delete=models.CASCADE, related_name='origin')
    destination = models.ForeignKey(SpaceStations, on_delete=models.CASCADE, related_name='destination')
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='PENDING')
    shipment_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(null=True, blank=True)
