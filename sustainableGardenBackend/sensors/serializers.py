from rest_framework import serializers
from .models import Sensor


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'created', 'sensor_name', 'sensor_type', 'pin', 'usb_port']
