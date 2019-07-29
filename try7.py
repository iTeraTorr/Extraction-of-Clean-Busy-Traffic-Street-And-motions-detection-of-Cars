import cv2
import numpy as np
cap=cv2.VideoCapture('road.mp4')
i=1507
rpre,pre=cap.read()
gpre=cv2.cvtColor(pre,cv2.COLOR_BGR2GRAY)
blurpre=cv2.GaussianBlur(gpre,(5,5),0)
ret6,thresh6=cv2.threshold(gpre,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret7,thresh7=cv2.threshold(blurpre,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('gaussian pre',thresh6)
cv2.imshow('gaussian blur pre',thresh7)
while(i):
    if i==1500:
        ret,img=cap.read()
        cv2.imshow('img',img)
    if i==1425:
        ret1,img1=cap.read()
        cv2.imshow('img1',img1)
    if i==1350:
        ret2,img2=cap.read()
        cv2.imshow('img2',img2)
    if i==1275:
        ret3,img3=cap.read()
        cv2.imshow('img3',img3)
    if i==1200:
        ret4,img4=cap.read()
        cv2.imshow('img4',img4)
    if i==1125:
        ret5,img5=cap.read()
        cv2.imshow('img5',img5)
    if i==1050:
        ret6,img6=cap.read()
        cv2.imshow('img6',img6)
    if i==975:
        ret7,img7=cap.read()
        cv2.imshow('img7',img7)
    if i==900:
        ret8,img8=cap.read()
        cv2.imshow('img8',img8)
    if i==825:
        ret9,img9=cap.read()
        cv2.imshow('img9',img9)
    if i==750:
        ret10,img10=cap.read()
        cv2.imshow('img10',img10)
    if i==675:
        ret11,img11=cap.read()
        cv2.imshow('img11',img11)
    if i==600:
        ret12,img12=cap.read()
        cv2.imshow('img12',img12)
    if i==575:
        ret13,img13=cap.read()
        cv2.imshow('img13',img13)
    if i==450:
        ret14,img14=cap.read()
        cv2.imshow('img14',img14)
    if i==375:
        ret15,img15=cap.read()
        cv2.imshow('img15',img15)
    if i==300:
        ret16,img16=cap.read()
        cv2.imshow('img16',img16)
    if i==225:
        ret17,img17=cap.read()
        cv2.imshow('img17',img17)
    if i==150:
        ret18,img18=cap.read()
        cv2.imshow('img18',img18)
    if i==75:
        ret19,img19=cap.read()
        cv2.imshow('img19',img19)
    ret20,frame20=cap.read()
    i-=1
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
cap.release()
temp1=cv2.addWeighted(img,0.05,img1,0.05,0)
cv2.imshow('temp1',temp1)
temp2=cv2.addWeighted(img2,0.05,img3,0.05,0)
cv2.imshow('temp2',temp2)
temp3=cv2.addWeighted(img4,0.05,img5,0.05,0)
cv2.imshow('temp3',temp3)
temp4=cv2.addWeighted(img6,0.05,img7,0.05,0)
cv2.imshow('temp4',temp4)
temp5=cv2.addWeighted(img8,0.05,img9,0.05,0)
cv2.imshow('temp5',temp5)
temp6=cv2.addWeighted(img10,0.05,img11,0.05,0)
cv2.imshow('temp6',temp6)
temp7=cv2.addWeighted(img12,0.05,img13,0.05,0)
cv2.imshow('temp7',temp7)
temp8=cv2.addWeighted(img14,0.05,img15,0.05,0)
cv2.imshow('temp8',temp8)
temp9=cv2.addWeighted(img16,0.05,img17,0.05,0)
cv2.imshow('temp9',temp9)
temp10=cv2.addWeighted(img18,0.05,img19,0.05,0)
cv2.imshow('temp10',temp10)
x1=cv2.add(temp1,temp2)
x2=cv2.add(temp3,temp4)
x3=cv2.add(temp5,temp6)
x4=cv2.add(temp7,temp8)
x5=cv2.add(temp9,temp10)
f1=cv2.add(x1,x2)
f2=cv2.add(x3,x4)
f3=cv2.add(x5,f2)
f=cv2.add(f3,f1)
cv2.imshow('f',f)
g=cv2.cvtColor(f,cv2.COLOR_BGR2GRAY)
cv2.imshow('g',g)
blur=cv2.GaussianBlur(g,(5,5),0)
ret6,thresh6=cv2.threshold(g,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret7,thresh7=cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('gaussian',thresh6)
cv2.imshow('gaussian blur',thresh7)
#cv2.destroyAllWindows()
