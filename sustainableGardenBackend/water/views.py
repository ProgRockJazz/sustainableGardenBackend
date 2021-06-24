from django.http import Http404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Valve
from .serializers import ValveSerializer
from .valve_open import ValveOpener


class ValveList(generics.ListCreateAPIView):
    """
    List all valves, or add a new valve.
    """
    queryset = Valve.objects.all()
    serializer_class = ValveSerializer


class ValveDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a valve.
    """
    queryset = Valve.objects.all()
    serializer_class = ValveSerializer


class ValveOpen(APIView):
    """
    Sends command to arduino to open valve
    """
    def get_object(self, pk):
        try:
            return Valve.objects.get(pk=pk)
        except Valve.DoesNotExist:
            raise Http404

    def get(self, request, pk, time):
        valve = self.get_object(pk)
        opener = ValveOpener(valve)
        response = opener.open(time)
        return Response(response)
