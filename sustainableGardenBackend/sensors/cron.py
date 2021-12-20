import requests
import json
from .models import Sensor, SensorReading
from sustainableGardenBackend.settings import ALLOWED_HOSTS


def read_all_sensors():
    url = "http://" + ALLOWED_HOSTS[0] + ":8000/sensors/all/read"
    data = requests.get(url)

    readings = json.loads(data.content.decode())

    for reading in readings:
        sensor_pk = reading.pop('sensor_pk')
        sensor = Sensor.objects.get(pk=sensor_pk)
        reading = SensorReading(sensor=sensor, reading=reading)
        reading.save()
    

