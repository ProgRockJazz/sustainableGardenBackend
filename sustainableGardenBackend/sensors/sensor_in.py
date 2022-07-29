import serial
from serial.serialutil import SerialException
from .models import Sensor, SensorReading
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

def initialize_test_dependencies():
    hAndTSensor = Sensor.objects.create(
        sensor_name="Humidity and Temp",
        sensor_type="DHT11 - Humidity/Temperature",
        pin=7,
        usb_port="Arduino MEGA",
        in_use=True
    )
    SensorReading.objects.create(sensor=hAndTSensor, reading = {
        "Humidity": float,
        "Temperature": float
    })
    rainSensor = Sensor.objects.create(
        sensor_name="Rain",
        sensor_type="Rain Sensor",
        pin=8,
        usb_port="Arduino MEGA",
        in_use=True
    )
    SensorReading.objects.create(sensor=rainSensor, reading = {
        "Rain": int
    })
    soilSensor = Sensor.objects.create(
        sensor_name="SoilSensor",
        sensor_type="SoilSensor",
        pin=9,
        usb_port="Arduino MEGA",
        in_use=True
    )
    SensorReading.objects.create(sensor=soilSensor, reading = {
        "Soil": float
    })
