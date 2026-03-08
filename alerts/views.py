from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Alerts
from .serializers import AlertSerializer

class get_alerts(ListAPIView):
    queryset = Alerts.objects.all().order_by('-created_at')
    serializer_class = AlertSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'created_at': ['gte', 'lte'],
        'sensor_id': ['exact'],
        'sensor_id__device_id': ['exact'],
        'status' : ['exact'],
    }