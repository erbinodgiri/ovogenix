from django.db import models
from apps.devices.models import Device

class Alert(models.Model):
    ALERT_TYPES = (
        ('temperature', 'Temperature Anomaly'),
        ('humidity', 'Humidity Anomaly'),
        ('turning', 'Turning Issue'),
        ('discrepancy', 'Data Discrepancy'),
    )
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='alerts')
    alert_type = models.CharField(max_length=20, choices=ALERT_TYPES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.device.name} - {self.alert_type}"