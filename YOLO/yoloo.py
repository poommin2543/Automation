# from ultralytics import YOLO
# import cv2
# model = YOLO("C:/Users/Nnn/Documents/Automation/YOLO/best.pt")
# # cap = cv2.VideoCapture(1)
# img = cv2.imread("C:/Users/Nnn/Documents/Automation/YOLO/dataset/ok5.jpg", cv2.IMREAD_COLOR)
# output = model.predict(source=img,show = False)
# class_list = ["NG","OK"]
# for i in output:
#     print(i.boxes.conf)
#     print(i.boxes.cls)
#     print(class_list[int(i.boxes.cls)])
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# # while True:
# #     ret,frame = cap.read()
# #     model.predict(source=frame,show = True)
# #     cv2.waitKey(1)

from ultralytics import YOLO
import cv2
import socket
import time
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #TCP
s.connect(("192.168.137.171",80))
#PyTorch
cap = cv2.VideoCapture("C:/Users/Nnn/Documents/Automation/YOLO/bakery_automation.mp4")
model = YOLO("C:/Users/Nnn/Documents/Automation/YOLO/bakery.pt")
conf_score = []
while True:
    ret, frame = cap.read()
    res = model.predict(source = frame, show = True)

    for i in res:
        # Printing the confidence score of the prediction.
        # print(i.boxes.conf)
        lis = i.boxes.cls.tolist()
        print(lis)
        if lis != []:
            print(lis[0])
            s.send(bytes(str(int(lis[0])),'utf-8'))

    cv2.waitKey(1)
    
cv2.destroyAllWindows()