from django.urls import path
from .views import get_alerts

urlpatterns = [
    path('alerts/', get_alerts)
]

