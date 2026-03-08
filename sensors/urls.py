from django.urls import path
from .views import get_sensors_by_devices, get_sensor_by_id


urlpatterns = [
    path('devices/<int:device_id>/sensors/', get_sensors_by_devices),
    path('devices/<int:device_id>/sensors/<int:sensor_id>/', get_sensor_by_id)
]
