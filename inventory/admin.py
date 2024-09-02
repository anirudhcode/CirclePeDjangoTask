from django.contrib import admin
from .models import Inventory

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['productName', 'quantity', 'created_at']
    search_fields = ['item']
    list_filter = ['created_at']
    readonly_fields = ['id', 'created_at', 'updated_at']
    ordering = ['created_at']
    list_per_page = 10