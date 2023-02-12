#import machine
from machine import TouchPad,Pin
#import esp32
from time import sleep

led = Pin(13,Pin.OUT)
t = TouchPad(Pin(4))
#t.config(500)
#esp32.wake_on_touch(True)
#machine.sleep()

# t.config(600)  # I think 0 is default sensitivity and higher is less sensitive
# #t.read()
while True:
    print(t.read())
    sleep(0.1)
    if (t.read()<100):
        led.value(1)
        #sleep(0.1)
    else:
        led.value(0)