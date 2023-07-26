from rest_framework import routers
from .views import ElevatorViewset, ElevatorRetrieveViewset

elevator_router = routers.DefaultRouter()

elevator_router.register('elevator', ElevatorViewset, basename = 'elevator')
elevator_router.register('elev_retr', ElevatorRetrieveViewset, basename= 'elev_retr')