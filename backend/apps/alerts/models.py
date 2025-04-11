# backend/apps/alerts/models.py
from django.db import models
from apps.devices.models import Device

class Alert(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='alerts')
    type = models.CharField(max_length=50)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} - {self.device.device_id}"