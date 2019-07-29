import cv2
import numpy as np
def draw(event,x,y,flags,param):
    if event==cv2.EVENT_MOUSEMOVE+cv2.EVENT_FLAG_LBUTTON:
        cv2.circle(img,(x,y),1,(255,255,255),1)
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('img')
cv2.setMouseCallback('img',draw)
while(1):
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF==27:
        break
cv2.destroyAllWindows
#import cv2
#events = [i for i in dir(cv2) if 'EVENT' in i]
#print events
