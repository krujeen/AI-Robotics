import torch
import cv2
import numpy as np

# vid = cv2.VideoCapture(0)
vid = cv2.VideoCapture("rtsp://admin:passwordd@192.168.1.2:554/stream1")

while(True):
    ret, frame = vid.read()
    cv2.imshow('YOLO', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
