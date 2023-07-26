#Python imports
#3rd party imports
import json
from django.shortcuts import render
from rest_framework import viewsets,mixins, status, response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
#Local imports
from .models import Elevator
from .serializers import ElevatorSerializers
from .services import on_called

class ElevatorViewset(viewsets.GenericViewSet,mixins.ListModelMixin):
    """
        List of all elevators present 
    """
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']

    def post(self,request):
        """
            To create new elevator 
        """
        serializer = ElevatorSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['POST'],detail=False)
    def call_elevator(self,request):
        """
            Call an elevator with current floor and destination floor
        """
        payload = json.loads(request.body.decode('utf-8'))
        try:
            elevator_id = int(payload.get('elevator_id'))
            current_floor = int(payload.get('current_floor'))
            destination_floor = int(payload.get('destination_floor'))
        except Exception as e:
            return response.Response({'error': 'Missing or bad parameters'}, status=status.HTTP_400_BAD_REQUEST)

        request_status = on_called(elevator_id, current_floor, destination_floor)
        payload = {
            'elevator_id': elevator_id,
            'request_status': request_status
        }
        return response.Response(payload,status=status.HTTP_200_OK)
        

class ElevatorRetrieveViewset(viewsets.GenericViewSet,mixins.RetrieveModelMixin):
    """
        Retrieve elevator details using id 
    """
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializers