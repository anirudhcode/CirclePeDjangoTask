from django.db import models
import uuid 

STATUS_CHOICES = [
    ('INITIATED', 'INITIATED'),
    ('DELIVERED', 'DELIVERED'),
    ('CANCELLED', 'CANCELLED'),
]
PAYMENT_CHOICES = [
    ('PENDING', 'PENDING'),
    ('PAID', 'PAID'),
]

class Trade(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    seller = models.ForeignKey('spacestations.SpaceStations', on_delete=models.CASCADE, related_name='seller')
    buyer = models.ForeignKey('spacestations.SpaceStations', on_delete=models.CASCADE, related_name='buyer')
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='INITIATED')
    payment_status = models.CharField(max_length=255, choices=PAYMENT_CHOICES, default='PENDING')
    amount = models.FloatField() #Or CharField if we assume no central currency system
    cargo = models.OneToOneField('cargo.Cargo', on_delete=models.SET_NULL, related_name='trade', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.seller.name} - {self.buyer.name}'
    
