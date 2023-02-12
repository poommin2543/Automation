from ultralytics import YOLO
import cv2
model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture(1)
while True:
    ret,frame = cap.read()
    model.predict(source=frame,show = True)
    cv2.waitKey(1)