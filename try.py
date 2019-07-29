import cv2
import numpy as np
from matplotlib import pyplot as plt

cap=cv2.VideoCapture(0)
while(True):
    ret,frame=cap.read()
    img=cv2.imread(frame,0)
    ret1,thresh=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
    cv2.imshow('thresh',thresh)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
