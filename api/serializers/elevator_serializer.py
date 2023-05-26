from rest_framework import serializers
from api.models import Elevator

class ElevatorSerializer(serializers.ModelSerializer):
    """Serializer for Elevator"""

    class Meta:
        model = Elevator
        exclude = ('created_at', 'updated_at')