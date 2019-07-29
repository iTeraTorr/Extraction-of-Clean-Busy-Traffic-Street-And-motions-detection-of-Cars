import numpy as np
import cv2
import copy
# import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    median_blur=cv2.medianBlur(gray,5)
    ret1,thresh1=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    ret2,thresh2=cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
    ret3,thresh3=cv2.threshold(gray,127,255,cv2.THRESH_TRUNC)
    ret4,thresh4=cv2.threshold(gray,127,255,cv2.THRESH_TOZERO)
    ret5,thresh5=cv2.threshold(gray,127,255,cv2.THRESH_TOZERO_INV)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    ret6,thresh6=cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    ret7,thresh7=cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    thresh8=cv2.adaptiveThreshold(median_blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                                  cv2.THRESH_BINARY,11,2)
    thresh9=cv2.adaptiveThreshold(median_blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                                  cv2.THRESH_BINARY,11,2)
    thresh10=copy.deepcopy(thresh1)
    titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV','GRAY_OTSU','BLUR_OTSU','MEAN_ADAPTIVE','GAUSSIAN_ADAPTIVE','DEEP_COPY']
    images = [gray, thresh1, thresh2, thresh3, thresh4, thresh5,thresh6,thresh7,thresh8,thresh9,thresh10]
    # Display the resulting frame
    for x in range(11):
     cv2.imshow(titles[x],images[x])
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
