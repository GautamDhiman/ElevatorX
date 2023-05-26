"""Viewset class for Elevator model."""

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from api.models import Elevator
from api.serializers import ElevatorSerializer


class ElevatorViewSet(viewsets.ModelViewSet):
    """Viewset class for Elevator model."""

    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

    @action(detail=True, methods=['GET'])
    def next_destination_floor(self, request, pk=None, elevator_system=None):
        """Fetch the next destination floor for a given elevator."""
        try:
            elevator = self.queryset.filter(elevator_system=elevator_system).get(pk=pk)
            next_floor = elevator.current_floor
            response = {}
            response['next_floor'] = next_floor
            response['elevator_system'] = elevator_system
            response['elevator'] = pk
            return Response(response)
        except Exception as e:
            return Response({'error': str(e)}, status=404)
