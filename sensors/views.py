from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Sensors
from .serializers import SensorSerializer

@api_view(['GET'])
def get_sensors_by_devices(request, device_id):
    sensors_data = Sensors.objects.filter(device_id=device_id)
    serializer = SensorSerializer(sensors_data, many=True)
    return Response(serializer.data)


