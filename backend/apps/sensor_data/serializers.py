from rest_framework import serializers
from .models import SensorData

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ['id', 'device', 'timestamp', 'temperature', 'humidity', 'turning', 'updated_by_staff']