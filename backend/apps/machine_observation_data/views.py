from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import HatcheryMachine, MachineObservationData
from .serializers import HatcheryMachineSerializer, MachineObservationDataSerializer

class MachineObservationCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.role != 'staff':
            return Response({'error': 'Only staff can enter observation data'}, status=403)
        serializer = MachineObservationDataSerializer(data=request.data)
        if serializer.is_valid():
            machine = serializer.validated_data['machine']
            if request.user not in machine.assigned_staff.all():
                return Response({'error': 'Not assigned to this machine'}, status=403)
            serializer.save(entered_by=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class MachineObservationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, machine_id):
        observations = MachineObservationData.objects.filter(machine_id=machine_id)
        if not observations.exists():
            return Response({'error': 'No data found'}, status=404)
        machine = observations.first().machine
        if request.user.role == 'client' and machine.owner != request.user:
            return Response({'error': 'Unauthorized'}, status=403)
        if request.user.role in ['consultant', 'staff'] and request.user not in machine.assigned_staff.all():
            return Response({'error': 'Unauthorized'}, status=403)
        serializer = MachineObservationDataSerializer(observations, many=True)
        return Response(serializer.data)