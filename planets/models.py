from django.db import models
import uuid
class Planets(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    localName = models.CharField(max_length=255)
    englishName = models.CharField(max_length=255)
    location = models.CharField(max_length=255) # IRL we would ideally use GeoSpatial fields using GeoDjango for this
    planetAttributes = models.JSONField(default=dict, null=True, blank=True) #In case we need parameters like atmosphere, gravity, etc.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
