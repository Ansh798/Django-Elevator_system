from django.contrib import admin
from .models import Elevator

@admin.register(Elevator)
class ElevatorAdmin(admin.ModelAdmin):
    list_display = ['current_floor','destination_floor','status','id']
