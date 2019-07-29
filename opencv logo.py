import cv2
import numpy as np
img=np.zeros((512,512,3),np.uint8)
img[:]=(255,255,255)
img=cv2.ellipse(img,(256,100),(60,60),90,30,330,(0,0,255),50)
img=cv2.ellipse(img,(160,266),(60,60),330,30,330,(0,255,0),50)
font=cv2.FONT_HERSHEY_SIMPLEX
img=cv2.putText(img,'OpenCV',(80,430),font,3,(0,0,0),9,cv2.LINE_AA)
img=cv2.ellipse(img,(256+96,266),(60,60),270,30,330,(255,0,0),50)
#img=cv2.line(img,(256,100),(160,266),(255,255,255),10)
#img=cv2.line(img,(256+96,266),(160,266),(255,255,255),10)
#img=cv2.line(img,(256+96,266),(256,100),(255,255,255),10)
cv2.imshow('k',img)
#img1=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#cv2.imshow('l',img1)
