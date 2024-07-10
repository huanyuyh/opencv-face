import cv2 as cv
src = cv.imread("C:/Users/17719/Pictures/321.png")
resize_image =cv.resize(src,dsize=(200,400))
cv.imshow("input image",resize_image)
cv.waitKey(0)
while True:
    if ord('q')==cv.waitKey(0):
        break
cv.destroyAllWindows()
