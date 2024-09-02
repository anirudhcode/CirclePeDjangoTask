from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
import json
from .models import Cargo
from events.models import Events
@receiver(post_save, sender=Cargo)
def cargo_post_save(sender, instance, created, **kwargs):
    event_type = 'CARGO_CREATED' if created else 'CARGO_UPDATED'
    Events.objects.create(
        event_type=event_type,
        details = json.dumps({
            'id': str(instance.id),
            'item': instance.item.productName,
            'volume': instance.volume,
            'weight': instance.weight,
            'destination': instance.destination.name,
            'status': instance.status,
        })
    )

@receiver(post_delete, sender=Cargo)
def cargo_post_delete(sender, instance, **kwargs):
    Events.objects.create(
        event_type='CARGO_DELETED',
        details = json.dumps({
            'id': str(instance.id),
            'item': instance.item.productName,
            'volume': instance.volume,
            'weight': instance.weight,
            'destination': instance.destination.name,
            'status': instance.status,
        })
    )
