import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('BGR',img)

# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)

# lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('LAB', lab)

# plt.imshow(img)
# plt.show()

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)
plt.imshow(rgb)
plt.show()







cv.waitKey(0)