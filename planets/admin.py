from django.contrib import admin
from .models import Planets

@admin.register(Planets)
class PlanetsAdmin(admin.ModelAdmin):
    list_display = ['localName', 'englishName', 'created_at']
    search_fields = ['localName', 'englishName']
    list_filter = ['created_at']
    readonly_fields = ['id', 'created_at', 'updated_at']
    ordering = ['created_at']
    list_per_page = 10
    