import cv2 as cv
def fac_detect_demo(img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    face_detector =cv.CascadeClassifier("C:/Users/17719/Downloads/opencv/sources/data/haarcascades_cuda/haarcascade_frontalface_default.xml")
    faces = face_detector.detectMultiScale(gray)
    for x,y,w,h in faces:
        cv.rectangle(img,(x,y),(x+w,y+h),color=(0,255,0),thickness=2)
        cv.imshow('result',img)

img = cv.imread("C:/Users/17719/Pictures/testface.jpg")
cv.imshow("img",img)
fac_detect_demo(img)
cv.waitKey(0)
cv.destroyAllWindows()