#Python imports
#3rd party imports
from django.shortcuts import render
from rest_framework import viewsets,mixins
#Local imports
from .models import Elevator
from .serializers import ElevatorSerializers

class ElevatorViewset(viewsets.GenericViewSet,mixins.ListModelMixin):
    """
        List of all elevators present 
    """
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializers


class ElevatorRetrieveViewset(viewsets.GenericViewSet,mixins.RetrieveModelMixin):
    """
        Retrieve elevator using id 
    """
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializers