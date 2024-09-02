from django.contrib import admin
from .models import Cargo

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'item', 'weight', 'volume', 'destination', 'shipment_date', 'delivery_date']
    search_fields = ['description', 'item', 'destination']
    list_filter = ['shipment_date', 'delivery_date']
    readonly_fields = ['id', 'shipment_date', 'delivery_date']
    ordering = ['shipment_date']
    list_per_page = 10