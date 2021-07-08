from rest_framework import serializers
from .models import Sensor, SensorReading


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'created', 'sensor_name', 'sensor_type', 'pin', 'usb_port', 'in_use']


class SensorReadingSerializer(serializers.ModelSerializer):
    sensor = SensorSerializer()

    class Meta:
        model = SensorReading
        fields = ['sensor', 'reading', 'time_of_reading']
