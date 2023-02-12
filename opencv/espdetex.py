import cv2
import numpy as np
import os
import time
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #TCP
s.connect(("192.168.137.224",80))

t = time.localtime()
current_time = time.strftime("%H%M%S", t)
print(current_time)
cap  = cv2.VideoCapture(1)
lower = np.array([10,130,150])
upper = np.array([30,255,255])

y = False
while True:
    ret,frame = cap.read()
    hsv = cv2.cvtColor(frame ,cv2.COLOR_BGR2HSV)  
    mark1 = cv2.inRange(hsv,lower,upper)
    c = cv2.waitKey(1)
    cv2.imshow("Cam",mark1)
    index = np.sum(mark1)
    # print(index)
    if index > 30000:
        y = True
    elif index < 30000:
        y = False
    s.send(bytes(str(y),'utf-8'))
    # s.send(bytes(str(current_time)+" => PC",'utf-8'))
    data = s.recv(1024)
    print(data.decode())

    if c == 27: #ascii Code 27 = esc
        os.chdir("C:\\Users\\Nnn\\Documents\\Automation\\opencv")
        cv2.imwrite(current_time+"NNN.jpg",mark1)
        break
cap.release()
cv2.destroyAllWindows()
