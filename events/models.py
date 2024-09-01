from django.db import models
import uuid 


class Events(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event_type = models.CharField(max_length=255) #Ideally this would be a choice field with a list of event types or even a foriegn key to a table of event types
    timestamp = models.DateTimeField()
    details = models.JSONField(default=dict, null=True, blank=True) #

    def __str__(self):
        return self.name
