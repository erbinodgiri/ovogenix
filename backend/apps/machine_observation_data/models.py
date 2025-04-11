from django.db import models
from apps.authentication.models import User

class HatcheryMachine(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the hatchery machine (e.g., Incubator A)")
    machine_id = models.CharField(max_length=50, unique=True, help_text="Unique identifier for the machine")
    location = models.CharField(max_length=100, help_text="Location within the hatchery")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hatchery_machines', help_text="Hatchery client who owns this machine")
    assigned_staff = models.ManyToManyField(User, related_name='assigned_machines', help_text="Staff assigned to monitor this machine")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Hatchery Machine"
        verbose_name_plural = "Hatchery Machines"

class MachineObservationData(models.Model):
    machine = models.ForeignKey(HatcheryMachine, on_delete=models.CASCADE, related_name='observation_data')
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField(help_text="Temperature in Celsius")
    humidity = models.FloatField(help_text="Humidity in percentage")
    turning = models.BooleanField(default=False, help_text="Whether the eggs were turned")
    entered_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='machine_observations', help_text="Staff who entered this data")

    def __str__(self):
        return f"{self.machine.name} - Observation at {self.timestamp}"

    class Meta:
        verbose_name = "Machine Observation Data"
        verbose_name_plural = "Machine Observation Data"