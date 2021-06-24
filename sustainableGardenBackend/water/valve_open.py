import serial
from .models import Valve
import json
import time


class ValveOpener:
    def __init__(self, valve: Valve):
        self.valve_info = {
            "pin": valve.pin,
        }
        self.usb = valve.usb_port

    def open(self, open_time):
        valve_send = self.valve_info
        valve_send["time"] = open_time
        valve_json = json.dumps(valve_send).encode('UTF-8')

        ser = serial.Serial(self.usb, 115200, timeout=1)
        time.sleep(2)
        ser.flush()

        ser.write(valve_json)
        return "Valve Opened!"
