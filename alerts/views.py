from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count, Q

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

@api_view(['GET'])
def get_alerts_of_device(request, id):
    device_queryset = Alerts.objects.filter(device_id=id)
    
    # Ab is filtered set par aggregation chalayein
    device_alerts = device_queryset.aggregate(
        total_device_alerts=Count('id'),
        critical=Count('id', filter=Q(status__iexact='critical')),
        warning=Count('id', filter=Q(status__iexact='warning'))
    )
    
    return Response(device_alerts)