import serial
from .models import Sensor
import json
import time


class SensorReader:
    def __init__(self, sensor: Sensor):
        self.sensor_info = {
            "sensor": sensor.sensor_type,
            "pin": sensor.pin
            
        }
        self.usb = sensor.usb_port

    def read(self):
        sensor_json = json.dumps(self.sensor_info).encode('UTF-8')

        ser = serial.Serial(self.usb, 115200, timeout=1)
        time.sleep(2)
        ser.flush()

        ser.write(sensor_json)
        time.sleep(1.5)
        out = ""
        while True:
            time.sleep(0.1)
            data = ser.readline().decode('utf-8').rstrip()
            if data:
                out += data
            else:
                out_json = json.loads(out)
                return out_json
