from rest_framework import serializers
from .models import Valve


class ValveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valve
        fields = ['id', 'created', 'valve_name', 'pin', 'usb_port']
