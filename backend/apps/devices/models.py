from django.db import models
from apps.authentication.models import User
from apps.machine_observation_data.models import HatcheryMachine

class Device(models.Model):
    name = models.CharField(max_length=100)
    device_id = models.CharField(max_length=50, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='devices')
    hatchery_machine = models.ForeignKey(HatcheryMachine, on_delete=models.SET_NULL, null=True, blank=True, related_name='ovogenix_devices', help_text="Hatchery machine this device is installed in")
    location = models.CharField(max_length=100)
    registered_at = models.DateTimeField(auto_now_add=True)
    assigned_users = models.ManyToManyField(User, related_name='assigned_devices', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ovogenix Device"
        verbose_name_plural = "Ovogenix Devices"