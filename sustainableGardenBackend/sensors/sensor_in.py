from json.decoder import JSONDecodeError
import serial
from serial.serialutil import SerialException
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
        data = ""
        out = ""
        out_json = ""
        ser = serial.Serial()
        ser.baudrate = 115200
        ser.timeout = 1
        ser.port = self.usb
        sensor_json = json.dumps(self.sensor_info).encode('UTF-8')
        try:
            ser.open()
        except (OSError, serial.SerialException):
            pass
        time.sleep(2)
        
        try:
            ser.flush()

            ser.write(sensor_json)
            time.sleep(1.5)
            data = ser.readline().decode('utf-8').rstrip()
        except (OSError, serial.SerialException):
            pass
        while True:
            time.sleep(0.1)
            if data:
                out += data
            else:
                try:
                    out_json = json.loads(out)
                except (JSONDecodeError):
                    pass
                break
        return out_json
