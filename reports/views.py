from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count, Q
from django.utils.timezone import now
from datetime import timedelta


from devices.models import Devices
from sensors.models import Sensors
from alerts.models import Alerts

@api_view(['GET'])
def get_reports(request):

    all_devices = Devices.objects.all()
    total_devices = all_devices.count()
    # Property use kar rahe hain jo humne model mein banayi thi
    active_devices = sum(1 for d in all_devices if d.device_status == "active")
        
    device_stats = {
        "total":total_devices,
        "active":active_devices,
        "inactive":(total_devices - active_devices)
    }

    all_sensors = Sensors.objects.all()
    total_sensors = all_sensors.count()
    active_sensors = sum(1 for s in all_sensors if s.sensor_status == "active")

    # sensors
    sensor_stats = {
        "total":total_sensors,
        "active":active_sensors,
        "inactive":(total_sensors - active_sensors)
    }

    # Current time minus 7 days
    seven_days_ago = now() - timedelta(days=7)

    # Alerts:
    alert_stats = Alerts.objects.aggregate(
        total=Count('id'),
        warning=Count('id', filter=Q(status__iexact='warning')),
        critical=Count('id', filter=Q(status__iexact='critical')),
        critical_last7days=Count('id', filter=Q(status__iexact='critical', created_at__gte=seven_days_ago)),
    )

    # Final Response Structure
    data = {
        "devices": device_stats,
        "sensors": sensor_stats,
        "alerts": alert_stats,
    }

    return Response(data)
