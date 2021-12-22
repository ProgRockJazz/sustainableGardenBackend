import serial
from serial.serialutil import SerialException
import time
import json
import sustainableGardenBackend

data = ""
out = ""
ser = serial.Serial()
ser.baudrate = 115200
ser.timeout = 1
ser.port ='com3' # change this to self.usb

sensor_data = open('/Users/Joseph Carey/Desktop/sustainableGardenBackend/sustainableGardenBackend/sensor_data_entry.json','r')
print(sensor_data)


sensor_load = json.loads(sensor_data.read())
print(sensor_load)
sensor_json = json.dumps(sensor_load).encode('UTF-8')
print(sensor_json)

try:
	ser.open()
except (OSError, serial.SerialException):
	print("exception passed")
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
		print(data)
	except (OSError, serial.SerialException):
		pass
	time.sleep(0.1)
	if data:
		print("I'm at the if statement! data exists!")
		print("out before: "+ out)
		out += data
		print("out after: " + out)
	else:
		print("No more data, loading out")
		out_json = json.loads(out)
		break

with open("/Users/Joseph Carey/Desktop/sustainableGardenBackend/sustainableGardenBackend/FinalData_sensors.json", "w") as outfile:
	json.dump(out_json, outfile)
