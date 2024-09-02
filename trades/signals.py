from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
import json
from .models import Trade
from events.models import Events

@receiver(post_save, sender=Trade)
def trade_post_save(sender, instance, created, **kwargs):
    event_type = 'TRADE_CREATED' if created else 'TRADE_UPDATED'
    Events.objects.create(
        event_type=event_type,
        details = json.dumps({
            'id': str(instance.id),
            'seller': instance.seller.name,
            'buyer': instance.buyer.name,
            'product': instance.cargo.item.productName if instance.cargo else None,
            'quantity': instance.cargo.volume if instance.cargo else None,
            'status': instance.status,
        })
    )

@receiver(post_delete, sender=Trade)
def trade_post_delete(sender, instance, **kwargs):
    Events.objects.create(
        event_type='TRADE_DELETED',
        details = json.dumps({
            'id': str(instance.id),
            'seller': instance.seller.name,
            'buyer': instance.buyer.name,
            'product': instance.product.name,
            'quantity': instance.quantity,
            'status': instance.status,
        })
    )
