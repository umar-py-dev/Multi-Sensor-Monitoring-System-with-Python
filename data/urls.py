from django.urls import path
from .views import get_sensor_data, DataFilterView

urlpatterns = [
    path('devices/<int:device_id_url>/sensors/<int:sensor_id_url>/data', get_sensor_data),
    path('filterData/', DataFilterView.as_view()),
]
