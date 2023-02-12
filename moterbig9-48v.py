from machine import Pin,PWM
from time import sleep

moterspeed = PWM(Pin(5),250)
Dir = Pin(19,Pin.OUT)
Enable = Pin(2,Pin.OUT)
while True:
    Enable.value(0)
    Dir.value(0)
    moterspeed.duty(512)