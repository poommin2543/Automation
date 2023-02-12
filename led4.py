# LED
from machine import Pin
import time
#Create an array of Pin15,Pin14,Pin13,Pin12 leds
leds = [Pin(13,Pin.OUT),Pin(12, Pin.OUT) , Pin (14, Pin.OUT) , Pin (27, Pin.OUT),Pin (14, Pin.OUT),Pin (12, Pin.OUT) ]
n=0
try:
    while True:
        for i in range (0,6):
            n = i
            leds[n].value(1)
            time.sleep_ms(500)
            leds[n].value(0)
            time.sleep_ms(500)
except KeyboardInterrupt:
        pass