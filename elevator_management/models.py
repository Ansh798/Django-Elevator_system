from django.db import models

class ElevatorStatus(models.TextChoices):
    MOVING = "moving"
    STOPPED = "stopped"
    IDLE = "idle"
    MAINTENANCE = "maintenance"


class Direction(models.TextChoices):
    UP = "up"
    DOWN = "down"
    STOP = "stop"

class Elevator(models.Model):

    is_operational = models.BooleanField(default=True)
    """Flag to check whether the elevator is operational or not"""

    current_floor = models.IntegerField()
    """Floor location where elevator is present"""

    destination_floor = models.IntegerField(null=True,blank=True)
    """Destination of the elevator"""

    status = models.CharField(max_length=50,choices=ElevatorStatus.choices,default=ElevatorStatus.MOVING)
    """Shows status of elevator"""

    direction = models.CharField(max_length=50,choices=Direction.choices,default=Direction.UP)
    """Choice for up or down of the elevator"""

    max_occupancy = models.IntegerField()
    """Number of maximum person on elevator"""

    current_occupancy = models.IntegerField()
    """current number of person on elevator"""

    min_floor = models.IntegerField()
    """Minimum floor elevator goes"""

    max_floor = models.IntegerField()
    """Maximum floor elevator goes"""

    def __str__(self) -> str:
        return self.status