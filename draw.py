import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype = 'uint8')


blank[:] = 0,255,0
blank[200:300, 300:400] = 255,0,0

cv.rectangle(blank,(0,0), (150,150), (0,0,255),thickness = -1)

cv.circle(blank, (150,400), 40, (255,0,255),thickness = 8)

cv.line(blank, (0,0), (250,250), (255,255,255), thickness = 3)



cv.putText(blank, "Ayush Kaushik", (100, 250), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,255), 2)





cv.imshow('Blank', blank)
cv.waitKey(0)