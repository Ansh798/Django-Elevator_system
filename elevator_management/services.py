from .models import Elevator, ElevatorStatus
import time

def move_elevator(elevator_id):
    """
    This function moves the elevator to the destination floor
    """
    elevator = Elevator.objects.get(id=elevator_id)
    if elevator.direction == 'up':
        while elevator.current_floor < elevator.destination_floor:
            elevator = Elevator.objects.get(id=elevator_id)
            elevator.current_floor += 1
            elevator.save()
            time.sleep(0.1)
    else:
        while elevator.current_floor > elevator.destination_floor:
            elevator = Elevator.objects.get(id=elevator_id)
            elevator.current_floor -= 1
            elevator.save()
            time.sleep(0.1)
    elevator.destination_floor = None
    elevator.status = ElevatorStatus.objects.get(status="idle")
    elevator.save()


def on_called(elevator_id, current_floor, destination_floor):
        """
        This is called when somebody presses the up or down button to call the elevator.
        This could happen at any time, whether or not the elevator is moving.
        The elevator could be requested at any floor at any time, going in either direction.
        elevator_id: the id of the elevator that the user intends to use
        current_floor: the floor that the elevator is being called to
        destination_floor: the destination floor the caller wants to go to
        """
        elevator = Elevator.objects.get(id=elevator_id,is_operational=True)

        if current_floor < elevator.min_floor or current_floor > elevator.max_floor:
            return "Current floor is not served by this elevator"
        if destination_floor < elevator.min_floor or destination_floor > elevator.max_floor:
            return "Destination floor is not served by this elevator"
        if elevator.status.status == "idle":
            call_when_idle(elevator_id, current_floor, destination_floor)
            move_elevator(elevator_id)
        elif elevator.status.status == "moving":
            elevator.status.status = "idle"
            call_when_idle(elevator_id, current_floor, destination_floor)
            move_elevator(elevator_id)
        elevator = Elevator.objects.get(id=elevator_id)
        return f"Request completed, elevator is at {elevator.current_floor} floor, and status is {elevator.status.status}"


def call_when_idle(elevator_id, current_floor, destination_floor):
    """
    This is called when the elevator is idle.
    """
    elevator = Elevator.objects.get(id=elevator_id)
    elevator.current_floor = current_floor
    elevator.destination_floor = destination_floor
    if destination_floor-current_floor > 0:
        elevator.direction = 'up'
    else:
        elevator.direction = 'down'
    elevator.status = ElevatorStatus.objects.get(status="moving")
    elevator.save()