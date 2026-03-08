from django.urls import path
from .views import get_all_devices, get_devices_data

urlpatterns = [
    path('devices/', get_all_devices),
    path('devices/<int:device_id_url>/', get_devices_data)
]