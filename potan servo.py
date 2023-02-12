from machine import Pin,ADC,PWM
from time import sleep

frequency = 50
servo = PWM(Pin(14), frequency)
pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB) #full range 3.3 V

while True:
    pot_value = pot.read()
    value = pot_value*(180/4095)
    servo.duty(int(value))
    print("%.2f"%value)
    sleep (0.1)
    
