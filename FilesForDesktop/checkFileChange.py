import os
import stat
import time
import datetime

fileStatsObj = os.stat ("/Users/Joseph Carey/Desktop/sustainableGardenBackend/sustainableGardenBackend/sensor_data_entry.json")
modificationTime = time.ctime ( fileStatsObj [ stat.ST_MTIME ] )
 
print("Last Modified Time : ", modificationTime )

startTime = ""

print("Running process...")

while True:
    fileStatsObj = os.stat ("/Users/Joseph Carey/Desktop/sustainableGardenBackend/sustainableGardenBackend/sensor_data_entry.json")
    modificationTime = time.ctime ( fileStatsObj [ stat.ST_MTIME ] )
    os.system("python getSerializedSensorData.py")

