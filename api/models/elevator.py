"""Model class for Elevator"""

from django.db import models
from api.models.base_model import BaseModel


class Elevator(BaseModel):
    """Model class for Elevator"""
    elevator_system = models.ForeignKey('ElevatorSystem', on_delete=models.CASCADE)
    elevator_number = models.IntegerField()
    current_floor = models.IntegerField()
    is_door_open = models.BooleanField(default=True)
    direction = models.CharField(choices=[(1, 'UP'), (-1, 'DOWN'), (0, 'STANDING STILL')], default=0)
    is_operational = models.BooleanField(default=True)

    def __str__(self):
        return self.elevator_number

    def save(self, *args, **kwargs):
        """overriding save method to auto increment elevator number."""

        if not self.pk:
            last_elevator_number = \
                Elevator.objects.filter(elevator_system=self.elevator_system).aggregate(Max('elevator_number'))[
                    'elevator_number__max']
            self.elevator_number = last_elevator_number + 1 if last_elevator_number is not None else 1
        super().save(*args, **kwargs)

    class Meta:
        """Meta class for Elevator"""

        db_table = 'elevator'
        ordering = ['elevator_number']
        verbose_name_plural = 'elevators'
