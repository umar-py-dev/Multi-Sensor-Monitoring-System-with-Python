from rest_framework import serializers
from .models import Sensors

class SensorSerializer(serializers.ModelSerializer):
    status = serializers.ReadOnlyField(source='sensor_status')
    class Meta:
        model = Sensors
        fields = ['id','sensor_type','unit','device_id','threshold_max_value','threshold_min_value','buffer_size','active_timeout','status', 'created_at' ]
