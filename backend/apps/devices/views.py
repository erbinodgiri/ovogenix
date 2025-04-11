from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Device
from .serializers import DeviceSerializer

class DeviceRegistrationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class DeviceListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        devices = Device.objects.filter(owner=request.user)
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)