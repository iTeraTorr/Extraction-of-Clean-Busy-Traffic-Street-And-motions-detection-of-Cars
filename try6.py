import cv2
import numpy as np
def nothing(x):
    pass
img=np.zeros((300,512,3),np.uint8)
img1=np.zeros((300,512,3),np.uint8)
cv2.namedWindow('image')
cv2.namedWindow('image1')
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)
cv2.createTrackbar('H','image1',0,225,nothing)
cv2.createTrackbar('S','image1',0,225,nothing)
cv2.createTrackbar('V','image1',0,225,nothing)

switch='0:OFF \n1:ON'
cv2.createTrackbar(switch,'image',0,1,nothing)
while(1):
    cv2.imshow('image',img)
    k=cv2.waitKey(1) & 0xFF
    if k==27:
        break
    r=cv2.getTrackbarPos('R','image')
    g=cv2.getTrackbarPos('G','image')
    b=cv2.getTrackbarPos('B','image')
    #h=cv2.getTrackbarPos('H','image1')
    #s=cv2.getTrackbarPos('S','image1')
    #v=cv2.getTrackbarPos('V','image1')
    img1=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h,s,v=img1[2,2]
    cv2.createTrackbar('H','image1',h,225,nothing)
    cv2.createTrackbar('S','image1',s,225,nothing)
    cv2.createTrackbar('V','image1',v,225,nothing)
    cv2.imshow('image1',img1)
    s=cv2.getTrackbarPos(switch,'image')
    if s==0:
        img[:]=0
    else:
        img[:]=[b,g,r]
cv2.destroyAllWindows()
     
