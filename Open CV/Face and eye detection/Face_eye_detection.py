# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 11:27:35 2021

@author: Sai Krishna
"""

#Importing libraries
import cv2
import os

#Setting directory
os.chdir('C:\\Data\\github\\python_projects\\Open CV\\Face and eye detection')

#Using the frontalface xml file
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

face_cascade.empty()
eye_cascade.empty()

#Selecting original image
img = cv2.imread('sachin-tendulkar.jpg')

cv2.imshow("sachin", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Detection corners of face and eyes
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
     cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
     roi_gray = gray[y:y+h, x:x+w]
     roi_color = img[y:y+h, x:x+w]
     eyes = eye_cascade.detectMultiScale(roi_gray)
     for (ex,ey,ew,eh) in eyes:
         cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

#Showing the output
cv2.imshow('sachin',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Saving the image
cv2.imwrite("sachin_face_eye_detected.png", img) 

