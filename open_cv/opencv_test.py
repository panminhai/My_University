import numpy as np
import cv2
import time

# カメラの使用を取得
cap = cv2.VideoCapture(0)

# 解析度設定
cap.set(3, 3840) # horizontal pixels
cap.set(4, 2160) # vertical pixels
cap.set(5, 15) # frame rate
time.sleep(2)

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow("captured video", frame)
    # waitKey:キーボード操作
    if cv2.waitKey(33) == ord('r'):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
    if cv2.waitKey(33) & 0xFF == ord('q'):
        break
cap.release()
cv2.destoryAllWindows()

"""
cam = cv2.VideoCapture(0)
w = cam.get(cv2.CV_CAP_PROP_FRAME_WIDTH)
h = cam.get(cv2.CV_CAP_PROP_FRAME_HEIGHT)
print(w, h)
while cam.isOpened():
    err, img = cam.read()
    cv2.imshow("lalala", img)
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break
"""    

