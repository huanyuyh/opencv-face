import cv2
import numpy as np
import face_recognition

img = face_recognition.load_image_file("C:/Users/17719/Downloads/jjy1.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
imgtest = face_recognition.load_image_file("C:/Users/17719/Downloads/jjy4.jpg")
imgtest = cv2.cvtColor(imgtest,cv2.COLOR_BGR2RGB)
faceLocs = face_recognition.face_locations(img)
encodeimg = face_recognition.face_encodings(img)[0]
for faceLoc in faceLocs:
    cv2.rectangle(img, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 0), 2)


faceTests = face_recognition.face_locations(imgtest)
encodeTest = face_recognition.face_encodings(imgtest)[0]
for faceLoc in faceTests:
    cv2.rectangle(imgtest, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 0), 2)
results = face_recognition.compare_faces([encodeimg],encodeTest)
faceDis = face_recognition.face_distance([encodeimg],encodeTest)
print(results,faceDis)
# result = face_recognition
cv2.imshow("test",img)
cv2.imshow("test1",imgtest)
cv2.waitKey(0)