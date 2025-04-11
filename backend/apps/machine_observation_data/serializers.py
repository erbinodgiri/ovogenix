from rest_framework import serializers
from .models import HatcheryMachine, MachineObservationData
from apps.devices.serializers import DeviceSerializer

class HatcheryMachineSerializer(serializers.ModelSerializer):
    ovogenix_devices = DeviceSerializer(many=True, read_only=True)

    class Meta:
        model = HatcheryMachine
        fields = ['id', 'name', 'machine_id', 'location', 'owner', 'assigned_staff', 'ovogenix_devices']
        read_only_fields = ['owner']

class MachineObservationDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineObservationData
        fields = ['id', 'machine', 'timestamp', 'temperature', 'humidity', 'turning', 'entered_by']
        read_only_fields = ['timestamp', 'entered_by']