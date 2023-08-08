

from django.contrib import admin
from django.urls import path, include


from elevator_management.urls import elevator_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(elevator_router.urls))
]
