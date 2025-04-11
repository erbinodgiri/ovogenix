from django.contrib import admin
from .models import Alert

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('device_name', 'alert_type', 'message', 'created_at', 'resolved')
    list_filter = ('alert_type', 'resolved', 'created_at', 'device__owner')
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
        updated = queryset.update(resolved=True)
        self.message_user(request, f"{updated} alerts marked as resolved.")
    mark_as_resolved.short_description = "Mark selected alerts as resolved"