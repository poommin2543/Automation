from machine import Pin,ADC
from time import sleep

pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB) #full range 3.3 V

while True:
    pot_value = pot.read()
    value = pot_value*(3.3/4095)
    print("%.2f V."%value)
    sleep (0.1)
    