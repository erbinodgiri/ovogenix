# backend/apps/devices/admin.py
from django.contrib import admin
from .models import Device

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['device_id', 'owner', 'created_at']  # Match model fields
    list_filter = ['owner', 'created_at']  # Valid fields only
    date_hierarchy = 'created_at'  # Now exists
    search_fields = ['device_id', 'name']