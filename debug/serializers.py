from rest_framework import serializers
from .models import DebugLog

class DebugSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebugLog
        fields = "__all__"