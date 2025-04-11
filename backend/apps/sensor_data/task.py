from celery import shared_task
from .models import SensorData
from apps.alerts.models import Alert

@shared_task
def process_sensor_data():
    for data in SensorData.objects.filter(processed=False):
        if data.temperature > 30:
            Alert.objects.create(
                device=data.device,
                alert_type='temperature',
                message=f"Temperature too high: {data.temperature}°C"
            )
        if data.humidity < 40:
            Alert.objects.create(
                device=data.device,
                alert_type='humidity',
                message=f"Humidity too low: {data.humidity}%"
            )
        data.processed = True
        data.save()
    return "Processed sensor data"