from django.contrib import admin
from .models import Alert

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('device', 'type', 'message', 'timestamp')
    list_filter = ('type', 'timestamp', 'device__device_id')  # Use device_id, not owner
    search_fields = ('message',)