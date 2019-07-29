import cv2
import numpy as np
img=cv2.imread('house.jpg')
#cv2.imshow('g',img)
res=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_LINEAR  )
#cv2.imshow('res',res)
h,w=img.shape[:2]
res=cv2.resize(img,(2*w,2*h),interpolation=cv2.INTER_CUBIC)
#cv2.imshow('res2',res)
M=np.float32([[1,0,100],[0,1,50]])
dst=cv2.warpAffine(img,M,(w,h))
#cv2.imshow('dst',dst)
N=cv2.getRotationMatrix2D((w/2,h/2),45,1)
dst=cv2.warpAffine(img,N,(w,h))
#cv2.imshow('k',dst)
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M=cv2.getAffineTransform(pts1,pts2)
dst=cv2.warpAffine(img,M,(w,h))
#cv2.imshow('mko',dst)
img1=cv2.imread('perspective.jpeg')
print(img1.shape)
#img1[123,478]=[255,255,255]
#img1[402,446]=[255,255,255]
#img1[117,797]=[255,255,255]
#img1[406,829]=[255,255,255]
cv2.imshow('img',img1)
pts1=np.float32([[478,123],[446,402],[797,117],[829,406]])
pts2=np.float32([[0,0],[0,300],[300,0],[300,300]])
M=cv2.getPerspectiveTransform(pts1,pts2)
dst=cv2.warpPerspective(img1,M,(300,300))
cv2.imshow('pers',dst)


