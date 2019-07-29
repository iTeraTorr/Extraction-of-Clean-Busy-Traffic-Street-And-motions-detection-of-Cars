import cv2
import numpy as np
img1=np.zeros((194,259,3),np.uint8)
img1[:]=(255,255,255)
img=cv2.imread('messi.jpg')
img1[0:194,0:259]=img[0:194,0:259]
#cv2.imshow('h',img)
img[:,:,2]=0
#cv2.imshow('k',img)
b,g,r=cv2.split(img)
#cv2.imshow('g',g)
#cv2.imshow('b',b)
#cv2.imshow('r',r)
ball=img[164:192,150:175]
img[164:192,70:95]=ball
#cv2.imshow('bm',img)
print(img.size)
print(img.shape)
#cv2.imshow('l',img1)
replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=[0,0,255])
#cv2.imshow('rep',replicate)
#cv2.imshow('ref',reflect)
#cv2.imshow('wrap',wrap)
#cv2.imshow('ref101',reflect101)
#cv2.imshow('constant',constant)
logo=cv2.imread('logo.png')
addfc=cv2.imread('addfc.png')
#cv2.imshow('logo',logo)
#cv2.imshow('addfc',addfc)
rows,cols,cha=logo.shape
roi=addfc[0:rows,0:cols]
logogray=cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)
ret,mask=cv2.threshold(logogray,150,255,cv2.THRESH_BINARY)
mask_inv=cv2.bitwise_not(mask)
cv2.imshow('mask',mask)
cv2.imshow('mask_inv',mask_inv)
addfc_bg=cv2.bitwise_and(roi,roi,mask=mask)
cv2.imshow('addfc_bg',addfc_bg)
logo_fg=cv2.bitwise_and(logo,logo,mask=mask_inv)
cv2.imshow('logo_fg',logo_fg)
dst=cv2.add(addfc_bg,logo_fg)
cv2.imshow('dst',dst)
addfc[0:rows,0:cols]=dst
cv2.imshow('addfc1',addfc)
cv2.imwrite('addfc1.jpg',addfc)
