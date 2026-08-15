import cv2 as cv
import numpy as np

img =  cv.imread('Resources/Photos/park.jpg')
cv.imshow('Img',img)


blank = np.zeros(img.shape[:2], dtype = 'uint8')

b,g,r = cv.split(img)
cv.imshow('Blue',b)
cv.imshow('Green',g)
cv.imshow('Red',r)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])




cv.imshow('Blue2',blue)
cv.imshow('Green2',green)
cv.imshow('Red2',red)








cv.waitKey()
