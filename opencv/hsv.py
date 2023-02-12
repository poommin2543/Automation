import cv2
import numpy as np
# img = cv2.imread("C:/Users/Nnn/Documents/Automation/opencv/My_Melo_greets_Kuromi_and_Baku_while_they_scape.jpg")
img = cv2.imread("C:/Users/Nnn/Documents/Automation/opencv/moises-de-paula-HPZZHJ-LuDI-unsplash.jpg")
# img = cv2.imread("C:/Users/Nnn/Documents/Automation/opencv/Which-color-converts-best.png")
# img = cv2.imread("C:\\Users\\Nnn\\Pictures\\IMG_8208.JPG")
rows,cols,_=img.shape
img = cv2.resize(img, None, fx = 0.5, fy = 0.5, interpolation= cv2.INTER_LINEAR)
hsv = cv2.cvtColor(img ,cv2.COLOR_BGR2HSV)  
 # Added this line of code to convert RGB color to GRAYSCALE  
gray_scale=cv2.cvtColor(img ,cv2.COLOR_BGR2GRAY)  

ret, thres = cv2.threshold(gray_scale,150,255,cv2.THRESH_BINARY)

kernel = np.ones((3,3),np.uint8)
print(kernel)

eroded = cv2.erode(thres , kernel, iterations = 1)
dilated = cv2.dilate(thres , kernel, iterations = 1)

# lower1 = np.array([0,0,0])
# upper1 = np.array([15,255,255])

# lower2 = np.array([165,0,0])
# upper2 = np.array([180,255,255])

# mark1 = cv2.inRange(hsv,lower1,upper1)
# mark2 = cv2.inRange(hsv,lower2,upper2)
# sum_mark = cv2.add(mark1,mark2)
# eroded = cv2.erode(sum_mark , kernel, iterations = 4)
lower = np.array([30,70,0])
upper = np.array([100,255,255])
mark1 = cv2.inRange(hsv,lower,upper)
eroded = cv2.erode(mark1 , kernel, iterations = 2)
dilated = cv2.dilate(eroded , kernel, iterations = 3)
cv2.imshow("img", img)
# cv2.imshow("hsv", hsv)
cv2.imshow("mark", mark1)
# cv2.imshow("eroded", eroded)
# cv2.imshow("dilated",dilated)

# cv2.imshow("rotated", gray_scale) 
# cv2.imshow("teres",thres) 
# cv2.imshow("erod",eroded)
cv2.waitKey(0)
cv2.destroyAllWindows()