import cv2
import numpy as np
cap=cv2.VideoCapture('road.mp4')
i=1507
n=[]
while(i):
    if i%50==0:
        ret,frame=cap.read()
        n.append(frame)
        print(i)
    ret20,frame20=cap.read()
    i-=1
    if cv2.waitKey(0) & 0xFF ==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
cv2.imshow('n29',n[29])
m=[]
for j in range(0,29,2):
    img=cv2.addWeighted(n[j],1/30,n[j+1],1/30,0)
    m.append(img)
add1=[]
for k in range(0,13,2):
    img1=cv2.add(m[k],m[k+1])
    add1.append(img1)
add1.append(m[14])
add2=[]
for l in range(0,7,2):
    img2=cv2.add(add1[l],add1[l+1])
    add2.append(img2)
f1=cv2.add(add2[0],add2[1])
f2=cv2.add(add2[2],add2[3])
f=cv2.add(f1,f2)
cv2.imshow('finally',f)

