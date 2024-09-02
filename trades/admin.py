from django.contrib import admin
from .models import Trade

@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'amount', 'created_at']
    search_fields = ['id']
    list_filter = ['created_at']
    readonly_fields = ['id', 'created_at']
    ordering = ['-created_at']
    list_per_page = 10
