from django.http import Http404
from sensors.sensor_in import SensorReader
from sensors.models import Sensor
from sensors.serializers import SensorSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response


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
    def get_object(self,pk):
        try:
            return Sensor.objects.get(pk=pk)
        except Sensor.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        sensor = self.get_object(pk)
        reader = SensorReader(sensor)
        data = reader.read()
        return Response(data)
