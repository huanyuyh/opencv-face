import cv2 as cv
src = cv.imread("C:/Users/17719/Pictures/321.png")
cv.imshow("input image",src)
gray_img = cv.cvtColor(src,code=cv.COLOR_BGR2GRAY)
cv.imshow('gray image',gray_img)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite('gray.png',gray_img)