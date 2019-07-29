import cv2
import numpy as np
def nothing(x):
    pass
img=cv2.imread('messi2.jpg')
cv2.namedWindow('dk')
cv2.createTrackbar('min','dk',0,500,nothing)
cv2.createTrackbar('max','dk',0,500,nothing)
cv2.imshow('dd',img)
while(1):
    m=cv2.getTrackbarPos('min','dk')
    M=cv2.getTrackbarPos('max','dk')
    img1=cv2.Canny(img,m,M)
    cv2.imshow('dk',img1)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

