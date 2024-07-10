import cv2 as cv

img = cv.imread("C:/Users/17719/Pictures/321.png")
cv.imshow('input image',img)
cv.waitKey(0)
cv.destroyAllWindows()