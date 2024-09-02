from django.contrib import admin
from .models import Events

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ['id', 'event_type', 'timestamp']
    search_fields = ['event_type']
    list_filter = ['timestamp']
    readonly_fields = ['id', 'timestamp']
    ordering = ['timestamp']
    list_per_page = 10