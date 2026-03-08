from rest_framework import serializers
from .models import Devices


class Device_serializer(serializers.ModelSerializer):
    status = serializers.ReadOnlyField(source='device_status')
    # ye config setting hen serialize krne ke liye...Main kam abi views me krna he..
    class Meta:
        model = Devices
        fields = ['id','name','device_type_id','location','status', 'created_at']