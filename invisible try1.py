import cv2
import numpy as np
def nothing(x):
    pass
cap=cv2.VideoCapture(0)
img=np.zeros((300,512,3),np.uint8)
#img[:]=(0,0,0)
cv2.namedWindow('rgb')
cv2.createTrackbar('R','rgb',0,255,nothing)
cv2.createTrackbar('G','rgb',0,255,nothing)
cv2.createTrackbar('B','rgb',0,255,nothing)
ret1,img1=cap.read()
print(img1.shape)
print('Wait For Magic!!!')
cv2.waitKey(5000)
while(1):
    ret,frame=cap.read()
    cv2.imshow('frame',frame)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow('rgb',img)
    r=cv2.getTrackbarPos('R','rgb')
    g=cv2.getTrackbarPos('G','rgb')
    b=cv2.getTrackbarPos('B','rgb')
    img[:]=[b,g,r]
    hsv1=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h,s,v=hsv1[2,2]
    lb=np.array([h-10,100,100],dtype=np.uint8)
    ub=np.array([h+10,255,255],dtype=np.uint8)
    mask=cv2.inRange(hsv,lb,ub)
    mask_inv=cv2.bitwise_not(mask)
    img2=cv2.bitwise_and(img1,img1,mask=mask)
    img3=cv2.bitwise_and(frame,frame,mask_inv)
    img4=cv2.add(img2,img3)
    cv2.imshow('magic',img4)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('res',mask)
    
    if cv2.waitKey(5) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
