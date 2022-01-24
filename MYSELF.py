import cv2
import numpy as np
import os
path = r'resources/irisler.jpeg' # Burada dosyanın asıl path'ini yapıştır. Sol panelden sağ tıkla -> copy -> absolutr path. Sonra yapıştır.
roi = cv2.imread(path)
gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
gray_blur = cv2.GaussianBlur(gray, (15, 15), 1)
canny_threshold_1=150
canny_threshold_2=100
gray_blur = cv2.Canny(gray_blur,canny_threshold_1,canny_threshold_2)
hough_param_1=20
hough_param_2=30
circles = cv2.HoughCircles(gray_blur,cv2.HOUGH_GRADIENT,1,50, param1=hough_param_1,param2=hough_param_2,minRadius=2,maxRadius=0)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
        cv2.circle(roi,(i[0],i[0]),i[2],(3,349,20),2)
        cv2.circle(roi, (i[1], i[1]),2, (1,1,10), 3)
cv2.imshow('Detected coins',roi)
cv2.imwrite('output/'+path,roi)




