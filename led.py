# from machine import Pin
# import time
# #Create an array of Pin15,Pin14,Pin13,Pin12 leds
# leds = [Pin(13,Pin.OUT),Pin(12, Pin.OUT) , Pin (14, Pin.OUT) , Pin (27, Pin.OUT),Pin (14, Pin.OUT),Pin (12, Pin.OUT) ]
# n=0
# try:
#     while True:
#         for i in range (0,6):
#             n = i
#             leds[n].value(1)
#             time.sleep_ms(500)
#             leds[n].value(0)
#             time.sleep_ms(500)
# except KeyboardInterrupt:
#         pass
#
# 
# from machine import Pin
# import time
# 
# button=Pin(12,Pin.IN, pull=1) #create Button object from pinl.#button=Pin(12,Pin.IN, pull=Pin.PULL_UP)
# led=Pin(5,Pin.OUT) #create LED object from pin5,Set PinS to outpr
# try:
#     while True:
#         
#         if (button.value() == 1):#Press button, value is 
#             led.value(1) #turn on
#         else:
#             led.value(0)
#             
# except KeyboardInterrupt:
#     pass

   
# 
# from machine import Pin, PWM
# import time
# 
# frequency = 5000 #set frequency
# 
# led = PWM(Pin(5), frequency) #create PWM object from pin5, Set frequen
# 
# try:
#     while True:
#         for duty_cycle in range(0, 1024): #duty cycle cycles between 0 and 1024
#             led.duty(duty_cycle) #duty cycle size of LED lights
#             time.sleep_ms(5) #delay of 2 ms
# except KeyboardInterrupt:
#     pass

#servo

# from machine import Pin, PWM
# import time
# frequency =50
# servo = PWM(Pin(14), frequency)
# try:
#     for i in range(50, 100):
#         servo.duty(i)
#         time.sleep_ms(10)
# except KeyboardInterrupt:
#     pass

from machine import Pin,ADC
from time import sleep

pot = ADC(Pin(34))
led1 = Pin(13,Pin.OUT)
led2 = Pin(12,Pin.OUT)
led3 = Pin(14,Pin.OUT)
pot.atten(ADC.ATTN_11DB) #full range 3.3 V

while True:
    pot_value = pot.read()
    value = pot_value*(3.3/4095)
    print("%.2f V."%value)
    sleep (0.1)
    if(value<0.3):
        led1.value(0)
        led2.value(0)
        led3.value(0)
        print("555")
    elif(value<1.3):
        led1.value(1)
        led2.value(0)
        led3.value(0)
        print("test")
    elif(value<2.3):
        led1.value(1)
        led2.value(1)
        led3.value(0)
        print("test")
    elif(value<3.3):
        led1.value(1)
        led2.value(1)
        led3.value(1)
        print("test")
    
    



