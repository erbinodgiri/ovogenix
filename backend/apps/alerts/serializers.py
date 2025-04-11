from rest_framework import serializers
from .models import Alert

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ['id', 'device', 'alert_type', 'message', 'created_at', 'resolved']
        read_only_fields = ['created_at']