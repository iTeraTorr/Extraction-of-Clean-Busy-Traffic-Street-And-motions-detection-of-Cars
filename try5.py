import cv2
import numpy
cap=cv2.VideoCapture(0)
ret1,img=cap.read()
while(True):
    ret,frame=cap.read()
    for x in range(100):
        for y in range(100):
            if str(frame[x,y])!=str(img[x,y]):
                img[x,y]=[0,0,255]
    cv2.imshow('frame',img)
    img=frame
    if cv2.waitKey(1) &0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
