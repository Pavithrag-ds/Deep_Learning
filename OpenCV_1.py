import cv2
import numpy as np

# Read an image
img = cv2.imread(r"C:\Users\PAVITHRA\Documents\Data Science Course\Course_7_Deep_Learning\Chapter_7\Train_Data\Sharuk2.jpg")
#################################################################################################################################

# Visulaize the image
cv2.imshow("My_Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()  #whenever you use waitkey fn,you must include this destroy fn line also otherwise it will get stuck
#################################################################################################################################

# RGB into Gray-scale Image(you will see the same image in black and white colour)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #convert the image from BlueGreenRed to Gray
cv2.imshow("My_Image",gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#################################################################################################################################

#Resize this image
Resized_img = cv2.resize(img,(350,400))
cv2.imshow("My_Image",Resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#################################################################################################################################

#Important Parameters
img.shape
Height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]
#################################################################################################################################

#Cropping of an image
Cropped_img = img[12:200,50:250]    #total Ht=300...here we ask for ht from 12 to 200(we crop remaining and get this part only )
cv2.imshow("My_Image",Cropped_img)  #total width=300...here we ask for ht from 50 to 250(we crop remaining and get this part only )
cv2.waitKey(0)
cv2.destroyAllWindows()
#################################################################################################################################

#Save this Cropped image
cv2.imwrite("Output_2026.jpg",Cropped_img)
#################################################################################################################################

#Apply Filters
Blurred_image = cv2.GaussianBlur(img,(7,7),2)  #If you increase the kernal size it will blurred more #Also we can adjust filters like 0,1,2
cv2.imshow("My_Image",Blurred_image)  
cv2.waitKey(0)
cv2.destroyAllWindows()
#################################################################################################################################

#Sharpenning the image 
Kernal = np.array([[-1,-1,-1],       #This array value is fixed taken from internet
                   [-1,9,-1],        #If you change these value you get a image according to those values
                   [-1,-1,-1]])
Sharpened_image = cv2.filter2D(img,-1, Kernal)
cv2.imshow("My_Image",Sharpened_image)  
cv2.waitKey(0)
cv2.destroyAllWindows()
#################################################################################################################################

#Apply the Canny edge detection Algorithm
edges = cv2.Canny(img,100,200)
cv2.imshow("My_Image",edges)  
cv2.waitKey(0)
cv2.destroyAllWindows()
#################################################################################################################################

#Flipping a image in different angle

center = (width/2,Height/2)
Angle_90 = 90
Angle_180 = 180
Angle_270 = 270
scale = 1.0 #(set as 1 because we no need to reduce or increase the dimensions)

x = cv2.getRotationMatrix2D(center, Angle_180, scale)

IMG_90 = cv2.warpAffine(img, x ,(Height,width))
cv2.imshow("My_Image",IMG_90)  
cv2.waitKey(0)
cv2.destroyAllWindows()

 




















