import numpy as np
import cv2
import copy
img=cv2.imread('hand.png')
imgg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(imgg,127,255,0)
contours,hierarchy=cv2.findContours(thresh,1,2)
cnt=contours[0]
print(type(contours))
M=cv2.moments(cnt)
print(M)
cx=int(M['m10']/M['m00'])
cy=int(M['m01']/M['m00'])
print(cx,cy)
x,y,w,h=cv2.boundingRect(cnt)
img5=cv2.rectangle(img.copy(),(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow('rect',img5)
# img2=cv2.drawContours(img,contours,0,(0,255,0),3)
# img2[83,117]=(0,0,0)
hull=cv2.convexHull(cnt)
print(cv2.isContourConvex(cnt))
img4=cv2.drawContours(img.copy(),[hull],-1,(0,255,0),3)
cv2.imshow('hull',img4)
print(type(hull))
area=cv2.contourArea(cnt)
perimeter=cv2.arcLength(cnt,True)
epsilon=0.043*cv2.arcLength(cnt,True)
# approx=cv2.approxPolyDP(cnt,epsilon,True)
approx=cv2.approxPolyDP(cnt,epsilon,True)
img3=cv2.drawContours(img,[approx],-1,(0,255,0),3)
print(type(approx),type(contours))
cv2.imshow('approx',img3)
print(area)
print(M['m00'],perimeter)
# cv2.imshow('con',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()