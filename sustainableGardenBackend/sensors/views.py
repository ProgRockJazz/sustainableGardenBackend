from django.http import Http404
from .sensor_in import SensorReader, initialize_test_dependencies
from .models import Sensor, SensorReading
from .serializers import SensorSerializer, SensorReadingSerializer
from rest_framework import generics
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
import serial.tools.list_ports

from datetime import datetime,timezone


class SensorList(generics.ListCreateAPIView):
    """
    List all sensors, or add a new sensor
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a sensor.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorRead(APIView):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        # for testing purposes: creates two Sensors and adds them to the database in in order
        # to make random SensorReadings
        
        initialize_test_dependencies()

    def get_object(self, pk):
        try:
            return Sensor.objects.get(pk=pk)
        except Sensor.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        sensor = self.get_object(pk)
        reader = SensorReader(sensor)
        data=reader.read()
        print("Data is: ")
        print(data)
        return Response(data)

class SensorReadAll(APIView):
    """
    View to read all current sensor values
    """

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        # for testing purposes: creates two Sensors and adds them to the database in in order
        # to make random SensorReadings            
        initialize_test_dependencies()

    def get(self, request):
        sensors = [sensor for sensor in Sensor.objects.all()]
        readings = []

        for sensor in sensors:
            reader = SensorReader(sensor)
            reading = reader.read()
            # reading["sensor_pk"] = sensor.pk
            newSensorReading = SensorReading(sensor = sensor, reading = reading, time_of_reading = datetime.now(timezone.utc))
            newSensorReading.save()
            newSerializerInstance = SensorReadingSerializer(newSensorReading)

            # readings.append(reading)
            readings.append(newSerializerInstance.data)

        return Response(readings)

class SensorReadingList(generics.ListAPIView):
    queryset = SensorReading.objects.order_by("time_of_reading")
    serializer_class = SensorReadingSerializer
