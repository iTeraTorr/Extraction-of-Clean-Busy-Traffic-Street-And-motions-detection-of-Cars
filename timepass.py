import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while(True):
    ret,frame=cap.read()
    rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    cv2.imshow('frame',rgb)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()