from django.db import models
from apps.machine_observation_data.models import HatcheryMachine

class Device(models.Model):
    hatchery_machine = models.ForeignKey(HatcheryMachine, on_delete=models.CASCADE, related_name='devices')
    device_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    owner = models.CharField(max_length=100, blank=True, null=True)  # Added
    created_at = models.DateTimeField(auto_now_add=True)  # Added

    def __str__(self):
        return self.device_id