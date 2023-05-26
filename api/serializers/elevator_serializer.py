from rest_framework import serializers
from api.models import Elevator

class ElevatorSerializer(serializers.ModelSerializer):
    """Serializer for Elevator"""

    class Meta:
        model = Elevator
        fields = '__all__'