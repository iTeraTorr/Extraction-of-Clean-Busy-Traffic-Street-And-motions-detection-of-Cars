import cv2
import numpy as np
img=np.zeros((512,512,3),np.uint8)
img[:]=(0,255,0)
img=cv2.line(img,(0,0),(126,128),(255,0,0),5)
img=cv2.line(img,(512,0),(384,128),(255,0,0),5)
img=cv2.rectangle(img,(384,2),(510,128),(100,50,100),3)
img=cv2.rectangle(img,(2,2),(126,128),(100,50,100),3)
img=cv2.ellipse(img,(256,409),(100,50),90,0,360,(0,0,255),5)
img=cv2.circle(img,(256,256),50,(0,0,255),-1)
pts=np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
pts=pts.reshape((-1,1,2))
img=cv2.polylines(img,[pts],True,(0,255,255))
font=cv2.FONT_HERSHEY_SIMPLEX
img=cv2.putText(img,'OpenCV',(10,500),font,1,(255,255,255),2,cv2.LINE_AA)
cv2.imshow('k',img)
    
