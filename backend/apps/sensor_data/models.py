from django.db import models
from apps.devices.models import Device
from apps.authentication.models import User

class SensorData(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='sensor_data')
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    turning = models.BooleanField(default=False)
    updated_by_staff = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='updated_sensor_data')

    def __str__(self):
        return f"{self.device.name} - {self.timestamp}"

    class Meta:
        verbose_name = "Sensor Data"
        verbose_name_plural = "Sensor Data"  # Already set, but verify