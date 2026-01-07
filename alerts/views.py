from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Alerts
from .serializers import AlertSerializer

@api_view(['GET'])
def get_alerts(request):
    alerts = Alerts.objects.all().order_by('-created_at')
    serializer = AlertSerializer(alerts, many=True)
    return Response(serializer.data)