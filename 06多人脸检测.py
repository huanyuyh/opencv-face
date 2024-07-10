import cv2 as cv
def fac_detect_demo(img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    face_detector =cv.CascadeClassifier("C:/Users/17719/Downloads/opencv/sources/data/haarcascades_cuda/haarcascade_frontalface_alt2.xml")
    faces = face_detector.detectMultiScale(gray,scaleFactor=1.02,minNeighbors=3,maxSize=(70,70),minSize=(40,40))
    for x,y,w,h in faces:
        print(x,y,w,h)
        cv.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
        cv.circle(img,center=(x+w//2,y+h//2),radius=w//2,color=(0,255,0),thickness=2)
        cv.imshow('result',img)

img = cv.imread("C:/Users/17719/Pictures/R123.jpg")
cv.imshow("img",img)
fac_detect_demo(img)
cv.waitKey(0)
cv.destroyAllWindows()