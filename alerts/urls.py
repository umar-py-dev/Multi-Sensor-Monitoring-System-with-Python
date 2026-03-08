from django.urls import path
from .views import get_alerts, get_alerts_of_device

urlpatterns = [
    path('alerts/', get_alerts.as_view()),
    path('device_alerts/<int:id>/', get_alerts_of_device)
]

