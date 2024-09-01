from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
import json
from .models import Cargo
from events.models import Event
@receiver(post_save, sender=Cargo)
def cargo_post_save(sender, instance, created, **kwargs):
    event_type = 'CARGO_CREATED' if created else 'CARGO_UPDATED'
    Event.objects.create(
        event_type=event_type,
        details = json.dumps({
            'id': str(instance.id),
            'item': instance.item.name,
            'volume': instance.volume,
            'weight': instance.weight,
            'origin': instance.origin.name,
            'destination': instance.destination.name,
            'status': instance.status,
        })
    )

@receiver(post_delete, sender=Cargo)
def cargo_post_delete(sender, instance, **kwargs):
    Event.objects.create(
        event_type='CARGO_DELETED',
        details = json.dumps({
            'id': str(instance.id),
            'item': instance.item.name,
            'volume': instance.volume,
            'weight': instance.weight,
            'origin': instance.origin.name,
            'destination': instance.destination.name,
            'status': instance.status,
        })
    )
