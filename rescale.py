import cv2 as cv


def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    capture.set(3,width)
    capture.set(4,height)



# img = cv.imread('Resources/Photos/Cat.jpg')
# cv.imshow('Cat', img)
# resizedCat = rescaleFrame(img)
# cv.imshow('Resized_Cat', resizedCat)
# cv.waitKey(0)

capture = cv.VideoCapture('Resources/Videos/Dog.mp4')

while True:
    isTrue, Frame = capture.read()
    resizedFrame = rescaleFrame(Frame)

    cv.imshow('Video', Frame)
    cv.imshow('Resize_Video', resizedFrame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()