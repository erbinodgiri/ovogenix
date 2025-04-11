from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.sensor_data.models import SensorData
from apps.alerts.models import Alert
from django.utils import timezone
from django.db.models import Avg

class DataSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        today = timezone.now().date()
        sensor_data = SensorData.objects.filter(timestamp__date=today)
        if request.user.role == 'client':
            sensor_data = sensor_data.filter(device__owner=request.user)
        elif request.user.role in ['consultant', 'staff']:
            sensor_data = sensor_data.filter(device__assigned_users=request.user)
        data = {
            'temperature_avg': sensor_data.aggregate(Avg('temperature'))['temperature__avg'],
            'humidity_avg': sensor_data.aggregate(Avg('humidity'))['humidity__avg'],
            'turning_count': sensor_data.filter(turning=True).count(),
        }
        return Response(data)

class AlertsSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        alerts = Alert.objects.filter(resolved=False)
        if request.user.role == 'client':
            alerts = alerts.filter(device__owner=request.user)
        elif request.user.role in ['consultant', 'staff']:
            alerts = alerts.filter(device__assigned_users=request.user)
        active_alerts = alerts.count()
        return Response({'active_alerts': active_alerts})