from machine import Pin
from time import sleep
import time
IN1 = Pin(26,Pin.OUT)
IN2 = Pin(25,Pin.OUT)
IN3 = Pin(33,Pin.OUT)
IN4 = Pin(32,Pin.OUT)

pins = [IN1, IN2, IN3, IN4]
sequence1 = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
sequence2 = [[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]
#sequence = [[1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1]]
timein = 20/2048/4
timeout = 10/2048/4
count = 0
timecount = time.time()
while True:
    
    while True:
        print(time.time()-timecount)
        for step in sequence1:
            count+=1
            for i in range(len(pins)):
                pins[i].value(step[i])
                sleep(timein)
            #print(count)
        if count==2048:
            break
    count = 0
    while True:
        print(time.time()-timecount)
        for step in sequence2:
            count+=1
            for i in range(len(pins)):
                pins[i].value(step[i])
                sleep(timeout)
            #print(count)
        if count==2048:
            break
    count = 0   
