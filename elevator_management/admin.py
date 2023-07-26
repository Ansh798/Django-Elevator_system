from django.contrib import admin
from .models import Elevator, ElevatorStatus

@admin.register(Elevator)
class ElevatorAdmin(admin.ModelAdmin):
    list_display = ['current_floor','destination_floor','status','id']

@admin.register(ElevatorStatus)
class ElevatorStatusAdmin(admin.ModelAdmin):
    list_display = ['id','status']