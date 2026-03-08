from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count, Q


from devices.models import Devices
from sensors.models import Sensors
from alerts.models import Alerts

@api_view(['GET'])
def get_reports(request):
        
    device_stats = Devices.objects.aggregate(
        total=Count('id'),
        active=Count('id', filter=Q(status__iexact='Active')),
        inactive=Count('id', filter=Q(status__iexact='Inactive'))
    )

    # sensors
    sensor_stats = Sensors.objects.aggregate(
        total=Count('id'),
        active=Count('id', filter=Q(status__iexact='Active')),
        inactive=Count('id', filter=Q(status__iexact='Inactive'))
    )

    # Alerts:
    alert_stats = Alerts.objects.aggregate(
        total=Count('id'),
        critical=Count('id', filter=Q(status__iexact='critical')),
        warning=Count('id', filter=Q(status__iexact='warning'))
    )

    # Final Response Structure
    data = {
        "devices": device_stats,
        "sensors": sensor_stats,
        "alerts": alert_stats,
    }

    return Response(data)
