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
        ser.port = 'com3'
        sensor_json = json.dumps(self.sensor_info).encode('UTF-8')
        print("The sensor info we are inputting is: ")
        print(sensor_json)
        try:
            ser.open()
        except (OSError, serial.SerialException):
            print("passing exception, is the port open?")
            print(ser.is_open)
            if ser.is_open == "False":
                self.is_open = True
                print(ser.is_open)
            pass
        time.sleep(2)
        
        try:
            ser.flush()

            ser.write(sensor_json)
            time.sleep(1.5)
        except (OSError, serial.SerialException):
            pass
        while True:
            try:
                data = ser.readline().decode('utf-8').rstrip()
                
            except (OSError, serial.SerialException):
                pass
            print(data)
            time.sleep(0.1)
            if data:
                print("I'm at the if statement! data exists!")
                print("out before: "+ out)
                out += data
                print("out after: " + out)
            else:
                try:
                    print("No more data, loading out: ")
                    print(out_json)
                    out_json = out
                except (JSONDecodeError):
                    pass
                break
        return out_json
