from django.contrib import admin
from .models import HatcheryMachine, MachineObservationData
from apps.devices.models import Device

class DeviceInline(admin.TabularInline):
    model = Device
    extra = 1
    fields = ('name', 'device_id', 'location', 'assigned_users')
    readonly_fields = ('registered_at',)

class MachineObservationDataInline(admin.TabularInline):
    model = MachineObservationData
    extra = 1
    fields = ('temperature', 'humidity', 'turning', 'entered_by')
    readonly_fields = ('timestamp',)

@admin.register(HatcheryMachine)
class HatcheryMachineAdmin(admin.ModelAdmin):
    list_display = ('name', 'machine_id', 'owner', 'location', 'assigned_staff_summary', 'ovogenix_device_count')
    list_filter = ('owner',)
    search_fields = ('name', 'machine_id', 'owner__username')
    filter_horizontal = ('assigned_staff',)
    inlines = [DeviceInline, MachineObservationDataInline]
    fieldsets = (
        (None, {
            'fields': ('name', 'machine_id', 'location'),
            'description': 'Details of the hatchery machine containing Ovogenix devices.'
        }),
        ('Ownership', {
            'fields': ('owner',),
            'description': 'Hatchery client who owns this machine.'
        }),
        ('Assignments', {
            'fields': ('assigned_staff',),
            'description': 'Staff assigned to enter observation data.'
        }),
    )

    def assigned_staff_summary(self, obj):
        return ", ".join([user.username for user in obj.assigned_staff.all()][:3]) + ("..." if obj.assigned_staff.count() > 3 else "")
    assigned_staff_summary.short_description = 'Assigned Staff'

    def ovogenix_device_count(self, obj):
        return obj.ovogenix_devices.count()
    ovogenix_device_count.short_description = 'Ovogenix Devices'

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)

@admin.register(MachineObservationData)
class MachineObservationDataAdmin(admin.ModelAdmin):
    list_display = ('machine_name', 'timestamp', 'temperature', 'humidity', 'turning', 'entered_by')
    list_filter = ('machine__owner', 'timestamp', 'entered_by')
    search_fields = ('machine__name', 'machine__machine_id')
    date_hierarchy = 'timestamp'
    ordering = ('-timestamp',)
    fieldsets = (
        (None, {
            'fields': ('machine', 'temperature', 'humidity', 'turning'),
            'description': 'Manual observation data for hatchery machines.'
        }),
        ('Staff Entry', {
            'fields': ('entered_by',),
            'description': 'Staff member who recorded this data.'
        }),
    )

    def machine_name(self, obj):
        return obj.machine.name
    machine_name.short_description = 'Machine'

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(machine__owner=request.user)