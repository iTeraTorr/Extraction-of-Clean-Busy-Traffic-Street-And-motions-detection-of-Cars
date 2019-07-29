import cv2
import numpy as np
def nothing(x):
    pass
cv2.setUseOptimized(True)
e1=cv2.getTickCount()
cap=cv2.VideoCapture('road.mp4')
i=1507
n=[]
print(cv2.useOptimized())
while(i):
    if i%20==0:
        ret,frame=cap.read()
        n.append(frame)
        print(i)
    ret20,frame20=cap.read()
    
    i-=1
    if cv2.waitKey(0) & 0xFF ==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
print(len(n))
cv2.imshow('n1',n[0])
m=[]
#cv2.imshow('n75',n[74])
for j in range(0,71,2):
    img=cv2.addWeighted(n[j],1/72,n[j+1],1/72,0)
    m.append(img)
add1=[]
for k in range(0,35,2):
    img1=cv2.add(m[k],m[k+1])
    add1.append(img1)
#add1.append(m[36])
print(len(add1))

addf=cv2.add(add1[0],add1[1])
for l in range(2,18):
    print(l)
    addf=cv2.add(addf,add1[l])
cv2.imshow('finally',addf)
cv2.imwrite('addfc.png',addf)
addfb=cv2.cvtColor(addf,cv2.COLOR_BGR2GRAY)
cv2.imwrite('addfb.png',addfb)
cap1=cv2.VideoCapture('road.mp4')
cv2.namedWindow('f')
cv2.createTrackbar('GrayScale','f',35,255,nothing)
i=1507
while(i):
    ret,frame=cap1.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    img=cv2.subtract(gray,addfb)
    img1=cv2.subtract(frame,addf)
    cv2.imshow('carscoloured',img1)
    cv2.imshow('cars',img)
    g=cv2.getTrackbarPos('GrayScale','f')
    ret,f=cv2.threshold(img,g,255,cv2.THRESH_BINARY)
    cv2.imshow('f',f)
    i-=1
    if cv2.waitKey(30) & 0xFF ==ord('q'):
        break
e2=cv2.getTickCount()
time=(e2-e1)/cv2.getTickFrequency()
print(time,e2-e1)
cap.release()
