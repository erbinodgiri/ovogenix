from rest_framework import serializers
from .models import Device

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'name', 'device_id', 'owner', 'hatchery_machine', 'location', 'registered_at', 'assigned_users']
        read_only_fields = ['owner', 'registered_at']