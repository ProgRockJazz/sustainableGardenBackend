from django.db import models

# usb_choices should be in a separate file
USB_CHOICES = [('/dev/ttyUSB0', 'USB Port 0'),
               ('/dev/ttyUSB1', 'USB Port 1'),
               ('/dev/ttyUSB2', 'USB Port 2'),
               ('/dev/ttyUSB3', 'USB Port 3'),
               ]


class Valve(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    valve_name = models.CharField(max_length=50, blank=True, default='')
    usb_port = models.CharField(choices=USB_CHOICES, default='/dev/ttyUSB0', max_length=50)
    pin = models.IntegerField()

    class Meta:
        ordering = ['valve_name']
