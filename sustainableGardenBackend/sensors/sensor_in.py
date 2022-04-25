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
        
        print("Sensor: ",self.sensor_info)
        with open("sensor_data_entry.json", "w") as outfile:
            json.dump(self.sensor_info, outfile)
        time.sleep(1)
        with open('FinalData_sensors.json') as json_file:
            data = json.load(json_file)
            print(data)


        print("Final data back is: ")
        print(data)
        return(data)

        #exclue pychache in gitignore
