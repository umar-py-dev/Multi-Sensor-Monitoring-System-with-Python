from django.urls import path
from .views import get_sensors_by_devices

urlpatterns = [
    path('devices/<int:device_id>/sensors/', get_sensors_by_devices)
]
