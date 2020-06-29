#Importing required libraries
import cv2

#Loading the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Capturing the video from the webcam
cap = cv2.VideoCapture(0)

while True:
    #Reading the frame
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    #Converting to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #Detecting the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 10)
    #Drawing a rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    #Output
    cv2.imshow("Detection", img)
    #Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

#Releasing the VideoCapture object
cap.release()


