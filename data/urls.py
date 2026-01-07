from django.urls import path
from .views import get_sensor_data
urlpatterns = [
    path('devices/<int:device_id_url>/sensors/<int:sensor_id_url>/', get_sensor_data)
]
