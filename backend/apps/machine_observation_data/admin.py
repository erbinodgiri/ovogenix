# backend/apps/machine_observation_data/admin.py
from django.contrib import admin
from .models import HatcheryMachine
from apps.devices.models import Device

class DeviceInline(admin.TabularInline):
    model = Device
    readonly_fields = ['device_id', 'name', 'location']  # Must match Device model fields
    extra = 0

@admin.register(HatcheryMachine)
class HatcheryMachineAdmin(admin.ModelAdmin):
    inlines = [DeviceInline]