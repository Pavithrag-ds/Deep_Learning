# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 09:02:11 2023

@author: Nasir
"""

import cv2
import numpy as np
########################################################################################
# Load an image
img = cv2.imread(r'C:\Users\Nasir\Facedect\image\Tom.jpg')

cv2.imshow('My Image', img)
# Wait for a key press
cv2.waitKey(0)
# Close the window
cv2.destroyAllWindows()

########################################################################################
# Convert an RGB image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('My Image', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

########################################################################################
# Resize an image
resized_img = cv2.resize(img, (640, 480))

cv2.imshow('My Image', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

########################################################################################
height=img.shape[0]
width=img.shape[1]
channels=img.shape[2]
size=img.size
print("Image Height---->",height)
print("Image Width--->",width)
print("Number of the chennals in image",channels)
print("Image Size-->",size)

########################################################################################
# Crop an image
cropped_img = img[12:200, 25:152]

cv2.imshow('My Image', cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

########################################################################################
# Save an image
cv2.imwrite('output.jpg', img)

########################################################################################

# Apply a Gaussian blur
blurred_img = cv2.GaussianBlur(img, (5, 5), 0)

cv2.imshow('My Image', blurred_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
########################################################################################

# image sharpning
kernel = np.array([[-1,-1,-1],
                   [-1, 9,-1],
                   [-1,-1,-1]])
sharpened_img = cv2.filter2D(img, -1, kernel)

cv2.imshow('My Image', sharpened_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

########################################################################################

# Apply the Canny edge detection algorithm
edges = cv2.Canny(img, 100, 200)

cv2.imshow('My Image', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

########################################################################################
# Apply an erosion operation
kernel = np.ones((5,5), np.uint8)
eroded_img = cv2.erode(img, kernel, iterations=1)

cv2.imshow('My Image', eroded_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

########################################################################################
(h,w)=img.shape[:2]
center=(w/2,h/2)
angle90=90
angle180=180
angle270=270
scale=1.0


M=cv2.getRotationMatrix2D(center,angle90,scale)
rotated90=cv2.warpAffine(img,M,(h,w))
cv2.imshow('My Image', rotated90)
cv2.waitKey(0)
cv2.destroyAllWindows()


M=cv2.getRotationMatrix2D(center,angle180,scale)
rotated180=cv2.warpAffine(img,M,(h,w))
cv2.imshow('My Image', rotated180)
cv2.waitKey(0)
cv2.destroyAllWindows()



M=cv2.getRotationMatrix2D(center,angle270,scale)
rotated270=cv2.warpAffine(img,M,(h,w))
cv2.imshow('My Image', rotated270)
cv2.waitKey(0)
cv2.destroyAllWindows()
