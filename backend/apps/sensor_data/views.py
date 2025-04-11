from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import SensorData
from .serializers import SensorDataSerializer

class SensorDataCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Only devices (IoT) should call this, but we'll assume authenticated for now
        serializer = SensorDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class SensorDataListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, device_id):
        sensor_data = SensorData.objects.filter(device_id=device_id)
        if request.user.role == 'client' and sensor_data.first().device.owner != request.user:
            return Response({'error': 'Unauthorized'}, status=403)
        if request.user.role in ['consultant', 'staff'] and request.user not in sensor_data.first().device.assigned_users.all():
            return Response({'error': 'Unauthorized'}, status=403)
        serializer = SensorDataSerializer(sensor_data, many=True)
        return Response(serializer.data)

class SensorDataUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, device_id):
        if request.user.role != 'staff':
            return Response({'error': 'Only staff can update sensor data'}, status=403)
        try:
            sensor_data = SensorData.objects.filter(device_id=device_id).latest('timestamp')
            if request.user not in sensor_data.device.assigned_users.all():
                return Response({'error': 'Not assigned to this device'}, status=403)
            serializer = SensorDataSerializer(sensor_data, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(updated_by_staff=request.user)
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except SensorData.DoesNotExist:
            return Response({'error': 'No sensor data found'}, status=404)