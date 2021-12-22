from django.http import Http404
from .sensor_in import SensorReader
from .models import Sensor, SensorReading
from .serializers import SensorSerializer, SensorReadingSerializer
from rest_framework import generics
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
import serial.tools.list_ports


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

    def get(self, request):
        sensors = [sensor for sensor in Sensor.objects.all()]
        readings = []

        for sensor in sensors:
            reader = SensorReader(sensor)
            reading = reader.read()
            reading["sensor_pk"] = sensor.pk
            readings.append(reading)

        return Response(readings)

class SensorReadingList(generics.ListAPIView):
    queryset = SensorReading.objects.all()
    serializer_class = SensorReadingSerializer
