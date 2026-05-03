# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:05:02 2023

@author: Nasir
"""
########################################################################################################
# Single Object 

import cv2

Front_face_dector=cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')

image=cv2.imread('C:/Users/Nasir/Facedect/image/shahrukh-khan_7.jpg')
cv2.imshow('image',image)
cv2.waitKey()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
face=Front_face_dector.detectMultiScale(gray)

for (x, y, w, h) in face:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
cv2.imshow('image',image)
cv2.waitKey()


########################################################################################################
# Multiple Objectss 
group_image=cv2.imread('C:/Users/Nasir/Facedect/image/Group_image.jpg')
cv2.imshow('image',group_image)
cv2.waitKey()

gray = cv2.cvtColor(group_image, cv2.COLOR_BGR2GRAY)
face=Front_face_dector.detectMultiScale(gray)

for (x, y, w, h) in face:
    cv2.rectangle(group_image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
cv2.imshow('image',group_image)
cv2.waitKey()

########################################################################################################
# WebCam

video=cv2.VideoCapture(0) # on the camera will capture the video

while True:
    success,frame=video.read()
    if success==True:
        gray_image=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = Front_face_dector.detectMultiScale(gray_image)
        for x,y,w,h in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
            cv2.imshow("web cam",frame)
            key=cv2.waitKey(5)
            if key==81 or key==113:
                break
    else:
        print("video is completed")





