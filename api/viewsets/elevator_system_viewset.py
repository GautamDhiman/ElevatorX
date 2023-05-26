"""Viewset for ElevatorSystem"""
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers import ElevatorSystemSerializer, ElevatorSerializer
from api.models import ElevatorSystem, Elevator

class ElevatorSystemViewSet(viewsets.ModelViewSet):
    """Viewset for ElevatorSystem"""

    queryset = ElevatorSystem.objects.all()
    serializer_class = ElevatorSystemSerializer

    @action(detail=False, methods=['GET'])
    def by_system_name(self, request, system_name=None):
        try:
            elevator_system = ElevatorSystem.objects.get(system_name=system_name)
            serializer = self.get_serializer(elevator_system)
            return Response(serializer.data)
        except ElevatorSystem.DoesNotExist:
            return Response({'error': 'Elevator system not found.'}, status=404)

