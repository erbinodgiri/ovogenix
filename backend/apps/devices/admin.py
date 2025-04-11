from django.contrib import admin
from .models import Device
from apps.sensor_data.models import SensorData

class SensorDataInline(admin.TabularInline):
    model = SensorData
    extra = 1
    fields = ('temperature', 'humidity', 'turning', 'updated_by_staff')
    readonly_fields = ('timestamp',)

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'device_id', 'owner', 'hatchery_machine_name', 'location', 'registered_at', 'assigned_users_summary')
    list_filter = ('owner', 'hatchery_machine', 'registered_at')
    search_fields = ('name', 'device_id', 'owner__username', 'hatchery_machine__name')
    filter_horizontal = ('assigned_users',)
    inlines = [SensorDataInline]
    fieldsets = (
        (None, {
            'fields': ('name', 'device_id', 'location'),
            'description': 'Basic information for an Ovogenix IoT device.'
        }),
        ('Placement', {
            'fields': ('hatchery_machine',),
            'description': 'Hatchery machine where this device is installed.'
        }),
        ('Ownership', {
            'fields': ('owner',),
            'description': 'Hatchery client who owns this device.'
        }),
        ('Assignments', {
            'fields': ('assigned_users',),
            'description': 'Assign consultants or staff to monitor this device.'
        }),
    )

    def hatchery_machine_name(self, obj):
        return obj.hatchery_machine.name if obj.hatchery_machine else "Unassigned"
    hatchery_machine_name.short_description = 'Hatchery Machine'

    def assigned_users_summary(self, obj):
        return ", ".join([user.username for user in obj.assigned_users.all()][:3]) + ("..." if obj.assigned_users.count() > 3 else "")
    assigned_users_summary.short_description = 'Assigned Users'

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)