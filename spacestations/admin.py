from django.contrib import admin
from .models import SpaceStations

@admin.register(SpaceStations)
class SpaceStationsAdmin(admin.ModelAdmin):
    list_display = ['name', 'planet', 'created_at']
    search_fields = ['name', 'planet']
    list_filter = ['created_at']
    readonly_fields = ['id', 'created_at', 'updated_at']
    ordering = ['created_at']
    list_per_page = 10
    