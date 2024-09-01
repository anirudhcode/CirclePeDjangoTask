from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
import json
from .models import Trade
from events.models import Event

@receiver(post_save, sender=Trade)
def trade_post_save(sender, instance, created, **kwargs):
    event_type = 'TRADE_CREATED' if created else 'TRADE_UPDATED'
    Event.objects.create(
        event_type=event_type,
        details = json.dumps({
            'id': str(instance.id),
            'spacestation': instance.spacestation.name,
            'product': instance.product.name,
            'quantity': instance.quantity,
            'status': instance.status,
        })
    )

@receiver(post_delete, sender=Trade)
def trade_post_delete(sender, instance, **kwargs):
    Event.objects.create(
        event_type='TRADE_DELETED',
        details = json.dumps({
            'id': str(instance.id),
            'spacestation': instance.spacestation.name,
            'product': instance.product.name,
            'quantity': instance.quantity,
            'status': instance.status,
        })
    )