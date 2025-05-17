import time
import cv2

cap = cv2.VideoCapture(0)
time.sleep(1)
ret, frame = cap.read()
cv2.imwrite("pic.jpg", frame)
