import cv2 as cv

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park', img)

#Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Gaussian Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#Edge Cascade
canny = cv.Canny(img, 125,175)
cv.imshow('Edge Detection', canny)
canny_blur = cv.Canny(blur, 125,175)
cv.imshow('Edge Detection blur', canny_blur)

#Dilating the Image
dilated = cv.dilate(canny_blur, (3,3), iterations=3)
cv.imshow("Dilate", dilated)

#Eroding
eroded = cv.erode(dilated,(3,3),iterations=3)
cv.imshow("Eroded", eroded)


cv.waitKey(0)