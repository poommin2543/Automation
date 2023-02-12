# in servo motor,
# 1ms pulse for 0 degree (LEFT)
# 1.5ms pulse for 90 degree (MIDDLE)
# 2ms pulse for 180 degree (RIGHT)

# so for 50hz, one frequency is 20ms
# duty cycle for 0 degree = (1/20)*100 = 5%
# duty cycle for 90 degree = (1.5/20)*100 = 7.5%
# duty cycle for 180 degree = (2/20)*100 = 10%

from machine import Pin, PWM
import time
frequency = 50
servo = PWM(Pin(14), frequency)
try:
    for i in range(0, 180):
        servo.duty(i)
        print(i)
        time.sleep_ms(10)
except KeyboardInterrupt:
    pass