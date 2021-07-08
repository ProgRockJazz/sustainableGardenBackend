from django.db import models

SENSOR_CHOICES = [('DHT11', 'DHT11 - Humidity/Temperature'),
                  ('Rain', 'Rain Sensor'),
                  ]

USB_CHOICES = [('/dev/ttyUSB0', 'USB Port 0'),
               ('/dev/ttyUSB1', 'USB Port 1'),
               ('/dev/ttyUSB2', 'USB Port 2'),
               ('/dev/ttyUSB3', 'USB Port 3'),
               ]


class Sensor(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    sensor_name = models.CharField(max_length=50, blank=True, default='')
    sensor_type = models.CharField(choices=SENSOR_CHOICES, default='DHT11', max_length=50)
    usb_port = models.CharField(choices=USB_CHOICES, default='/dev/ttyUSB0', max_length=50)
    pin = models.IntegerField()
    in_use = models.BooleanField(default=True)

    class Meta:
        ordering = ['sensor_name']


class SensorReading(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.PROTECT)
    reading = models.JSONField()
    time_of_reading = models.DateTimeField(auto_now_add=True)
