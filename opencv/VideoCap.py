import cv2
import numpy as np
import os
import time

t = time.localtime()
current_time = time.strftime("%H%M%S", t)
print(current_time)
cap  = cv2.VideoCapture(1)
lower = np.array([10,130,150])
upper = np.array([30,255,255])
# lower = np.array([105,170,150])
# upper = np.array([135,255,200])


while True:
    ret,frame = cap.read()
    hsv = cv2.cvtColor(frame ,cv2.COLOR_BGR2HSV)  
    mark1 = cv2.inRange(hsv,lower,upper)
    c = cv2.waitKey(1)
    cv2.imshow("Cam",mark1)
    index = np.sum(mark1)
    # print(index)
    if index > 30000:
        os.chdir("C:\\Users\\Nnn\\Documents\\Automation\\opencv")
        cv2.imwrite(current_time+"NNN.jpg",mark1)

    if c == 27: #ascii Code 27 = esc
        os.chdir("C:\\Users\\Nnn\\Documents\\Automation\\opencv")
        cv2.imwrite(current_time+"NNN.jpg",mark1)
        break
cap.release()
cv2.destroyAllWindows()
