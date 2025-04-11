from django.contrib import admin
from .models import SensorData

@admin.register(SensorData)
class SensorDataAdmin(admin.ModelAdmin):
    list_display = ('device_name', 'temperature', 'humidity', 'timestamp', 'processed')
    list_filter = ('device', 'timestamp', 'processed')
    search_fields = ('device__name',)
    date_hierarchy = 'timestamp'

    def device_name(self, obj):
        return obj.device.name
    device_name.short_description = 'Device'