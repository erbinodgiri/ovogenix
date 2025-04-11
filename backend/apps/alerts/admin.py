from django.contrib import admin
from .models import Alert

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('device_name', 'alert_type', 'message', 'created_at', 'resolved')
    list_filter = ('alert_type', 'resolved', 'created_at')
    search_fields = ('device__name', 'message')
    date_hierarchy = 'created_at'
    actions = ['mark_as_resolved']
    fieldsets = (
        (None, {
            'fields': ('device', 'alert_type', 'message', 'resolved'),
            'description': 'Alerts generated from sensor data anomalies or discrepancies.'
        }),
    )

    def device_name(self, obj):
        return obj.device.name
    device_name.short_description = 'Device'

    def mark_as_resolved(self, request, queryset):
        queryset.update(resolved=True)
    mark_as_resolved.short_description = "Mark selected alerts as resolved"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(device__owner=request.user)