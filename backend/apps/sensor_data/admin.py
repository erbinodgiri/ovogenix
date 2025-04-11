from django.contrib import admin
from .models import SensorData

@admin.register(SensorData)
class SensorDataAdmin(admin.ModelAdmin):
    list_display = ('device_name', 'timestamp', 'temperature', 'humidity', 'turning', 'updated_by_staff')
    list_filter = ('device__owner', 'timestamp', 'updated_by_staff')
    search_fields = ('device__name', 'device__device_id')
    date_hierarchy = 'timestamp'
    ordering = ('-timestamp',)
    fieldsets = (
        (None, {
            'fields': ('device', 'temperature', 'humidity', 'turning'),
            'description': 'Real-time sensor readings from Ovogenix devices.'
        }),
        ('Staff Updates', {
            'fields': ('updated_by_staff',),
            'description': 'Staff member who manually updated this data (if applicable).'
        }),
    )

    def device_name(self, obj):
        return obj.device.name
    device_name.short_description = 'Device'

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(device__owner=request.user)

    verbose_name = "Sensor Data"  # Explicitly set
    verbose_name_plural = "Sensor Data"