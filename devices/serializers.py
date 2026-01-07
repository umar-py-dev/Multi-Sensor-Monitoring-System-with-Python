from rest_framework import serializers
from .models import Devices


class Device_serializer(serializers.ModelSerializer):
    
    # ye config setting hen serialize krne ke liye...Main kam abi views me krna he..
    class Meta:
        model = Devices
        fields = '__all__'