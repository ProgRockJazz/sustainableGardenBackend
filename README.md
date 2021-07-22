# Sustainable Garden Backend

The backend brains for the GEAR club's sustainable garden project. The server is written with the [Django REST Framework](https://github.com/encode/django-rest-framework). It implements the ability to periodically read sensors from an arduino and store the readings. As well, it supports live readings of sensors and retrieving past readings through HTTP requests/reponses to the REST API. 

## Installation
Installation and deployment of the backend has two components:

### Django Server Setup
It is recommended to use [Docker](https://docs.docker.com/get-docker/) when deploying the Django backend and [Docker Compose](https://docs.docker.com/compose/install/) (included in Docker Desktop).

1. Clone github repo: 
```Bash
$ git clone https://github.com/paxman101/sustainableGardenBackend.git
$ cd sustainableGardenBackend/sustainableGardenBackend
```
2. Adjust Settings.py
3. Docker Compose:
```Bash
$ docker-compose up -d --build 
```
4. Initial Django Migration After Containers are Running:
```Bash
$ docker-compose exec web python manage.py migrate
```

### Arduino Setup
Use the [Arduino IDE](https://www.arduino.cc/en/software).
1. Download the Required Libraries Through Library Manager:  
[Example video](https://www.youtube.com/watch?v=GUTpaY1YaXo) of how to use the Library Manager  
>Required Libraries:  
>[ArduinoJson](https://github.com/bblanchon/ArduinoJson) by Benoit Blanchon  
>[DHT sensor library](https://github.com/adafruit/DHT-sensor-library) by Adafruit
2. Upload the program to the arduino
3. Connect arduino to server (Raspberry Pi) via USB

# Usage

# Troubleshooting
