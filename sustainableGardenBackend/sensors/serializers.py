from rest_framework import serializers
from sensors.models import Sensor, SENSOR_CHOICES


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'created', 'sensor_name', 'sensor_type', 'pin', 'usb_port']
