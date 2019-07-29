import cv2
import numpy as np
img =np.zeros((500,500,3),np.uint8)
img[:]=(0,0,255)
for i in range(60,255):
    for j in range(0,255):
        for k in range(0,255):
            img[:]=(i,j,k)
            cv2.imshow('k',img)
            if cv2.waitKey(1) & 0xFF ==ord('q'):
                break
            

