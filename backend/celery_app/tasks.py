from celery import shared_task
from apps.sensor_data.models import SensorData
from apps.alerts.models import Alert
from django.utils import timezone
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@shared_task
def process_sensor_data():
    recent_data = SensorData.objects.filter(timestamp__gte=timezone.now() - timezone.timedelta(minutes=5))
    channel_layer = get_channel_layer()
    for data in recent_data:
        if data.temperature > 40 or data.temperature < 20:
            alert = Alert.objects.create(device=data.device, alert_type='temperature', message=f"Temperature anomaly: {data.temperature}°C")
            async_to_sync(channel_layer.group_send)(
                f"alert_{data.device.owner.id}", {"type": "send_alert", "data": {"message": alert.message}}
            )
        if data.humidity > 80 or data.humidity < 20:
            alert = Alert.objects.create(device=data.device, alert_type='humidity', message=f"Humidity anomaly: {data.humidity}%")
            async_to_sync(channel_layer.group_send)(
                f"alert_{data.device.owner.id}", {"type": "send_alert", "data": {"message": alert.message}}
            )
        if data.updated_by_staff and (abs(data.temperature - data.temperature) > 5 or abs(data.humidity - data.humidity) > 10):
            alert = Alert.objects.create(device=data.device, alert_type='discrepancy', message="Staff update discrepancy detected")
            async_to_sync(channel_layer.group_send)(
                f"alert_{data.device.owner.id}", {"type": "send_alert", "data": {"message": alert.message}}
            )