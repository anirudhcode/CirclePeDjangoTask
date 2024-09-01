from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from spacestations.models import SpaceStations


class Users(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    spaceStation = models.ForeignKey(SpaceStations, on_delete=models.CASCADE, related_name='users', null=True, blank=True)
    designation = models.CharField(max_length=255, null=True, blank=True)
    extra_attributes = models.JSONField(default=dict, blank=True, null=True) #The alient user might come with a manual or warnings. who knows?
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
