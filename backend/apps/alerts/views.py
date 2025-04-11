from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Alert
from .serializers import AlertSerializer

class AlertListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        alerts = Alert.objects.filter(device__owner=request.user)
        serializer = AlertSerializer(alerts, many=True)
        return Response(serializer.data)

class AlertResolveView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, alert_id):
        try:
            alert = Alert.objects.get(id=alert_id, device__owner=request.user)
            alert.resolved = True
            alert.save()
            serializer = AlertSerializer(alert)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Alert.DoesNotExist:
            return Response({"error": "Alert not found or not authorized"}, status=status.HTTP_404_NOT_FOUND)