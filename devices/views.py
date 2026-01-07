from django.shortcuts import render

# ye btai ga ke only get kr skte hen ya post ya both... ye na ho ke user post krta rhe apna data:
from rest_framework.decorators import api_view

from rest_framework.response import Response
from .models import Devices
from .serializers import Device_serializer

# Create your views here.

@api_view(['GET'])
def get_all_devices(request):
    devices_data = Devices.objects.all()
    serializer = Device_serializer(devices_data, many=True)
    return Response(serializer.data)