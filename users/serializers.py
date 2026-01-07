from rest_framework import serializers
from .models import AppUsers

class LoginSerializer(serializers.Serializer):
        username = serializers.CharField()
        password = serializers.CharField()