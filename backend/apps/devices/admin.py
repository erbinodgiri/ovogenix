from django.contrib import admin
from .models import Device

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'owner', 'created_at', 'name', 'location')
    list_filter = ('owner', 'created_at')
    search_fields = ('device_id', 'name', 'location')
    date_hierarchy = 'created_at'