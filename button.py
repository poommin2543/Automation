from machine import Pin
import time

button=Pin(12,Pin.IN, pull=1) #create Button object from pinl.#button=Pin(12,Pin.IN, pull=Pin.PULL_UP)
led=Pin(5,Pin.OUT) #create LED object from pin5,Set PinS to outpr
try:
    while True:
        
        if (button.value() == 1):#Press button, value is 
            led.value(1) #turn on
        else:
            led.value(0)
            
except KeyboardInterrupt:
    pass

