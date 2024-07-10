import cv2 as cv
src = cv.imread("C:/Users/17719/Pictures/321.png")
x,y,w,h = 50,50,80,80
cv.rectangle(src,(x,y,x+w,x+y),color=(0,255,0),thickness=2)
x,y = 100,100
cv.circle(src,center=(x,y),radius=(100),color=(0,255,255))
cv.imshow('rectangle',src)
while True:
    if ord('q')==cv.waitKey(0):
        break
cv.destroyAllWindows()
