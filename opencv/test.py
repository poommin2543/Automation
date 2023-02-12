# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Nnn\\Pictures\\IMG_8208.JPG")
# rows,cols,_=img.shape
# # TRANSLATION
# # M = np.float32([[1,0,100],[0,1,100]])
# # trans = cv2.warpAffine(img,M,(cols,rows))
# # ROTATION
# center = (cols/2, rows/2)
# M = cv2.getRotationMatrix2D(center,45.0, 1.0)
# rot = cv2.warpAffine(img,M, (cols, rows))
# # FLIPPING
# # flipped = cv2.flip(img,1)
# # RESIZE
# # output = cv2.resize(img, None, fx = 0.5, fy = 0.5, interpolation= cv2.INTER_LINEAR)
# # HSV COLOR
# # hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #: Convert RGB color to HSV
# # hsv = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #: Convert RGB color to HSV

# cv2.imshow("img",rot)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Refactored code:
import cv2
import numpy as np
img = cv2.imread("C:\\Users\\Nnn\\Pictures\\IMG_8208.JPG")
rows,cols,_=img.shape
# TRANSLATION
M = np.float32([[1,0,100],[0,1,100]])
trans = cv2.warpAffine(img,M,(cols,rows))
# ROTATION
center = (cols/2, rows/2)
M = cv2.getRotationMatrix2D(center,45.0, 1.0)
rot = cv2.warpAffine(img,M, (cols, rows))
# FLIPPING
flipped = cv2.flip(img,1)  # Added this line of code to flip the image 
# RESIZE  # Added this line of code to resize the image 
output = cv2.resize(img, None, fx = 0.5, fy = 0.5, interpolation= cv2.INTER_LINEAR)  

 # Added this line of code to convert RGB color to HSV  
hsv = cv2.cvtColor(img ,cv2.COLOR_BGR2HSV)  

 # Added this line of code to convert RGB color to GRAYSCALE  
gray_scale=cv2.cvtColor(img ,cv2.COLOR_BGR2GRAY)  

  # Changed the order of displaying the images  
cv2.imshow("flipped", flipped)  # Displays the flipped image  
cv2.imshow("resized", output)  # Displays the resized image   
cv2.imshow("hsv", hsv)        # Displays the HSV image   								   				   	   	   	   	   	     # Displays the grayscale image    

  # Changed the order of displaying the images  
cv2.imshow("rotated", rot)     # Displays the rotated image  
cv2.imshow("rotated", gray_scale)  
  # Changed waitKey() parameter from 0 to 2000 so that it waits for
cv2.waitKey(0)
cv2.destroyAllWindows()