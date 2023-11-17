import cv2 
import matplotlib.pyplot as plt 
import numpy as np

img = cv2.imread("image/MAP.jpg")

thresh, re1 =  cv2.threshold(img,170,255,cv2.THRESH_BINARY_INV)
#การขยายภาพ
kernal = np.ones((2,2),np.uint8)

#การกร่อนภาพ 
erosion = cv2.erode(re1,kernal,iterations=3)

#Opening
opening = cv2.morphologyEx(re1,cv2.MORPH_OPEN,kernal,iterations=6)

#Closeing
Closeing = cv2.morphologyEx(re1,cv2.MORPH_CLOSE,kernal,iterations=5)

dilatetion = cv2.dilate(re1,kernal,iterations=3)

title = ["ORIGINAL","THRESH","DILATETION","ERODETION","OPENING","CLOSEING"]
image = [img,re1,dilatetion,erosion,opening,Closeing]

for i in range(len(image)):
    plt.subplot(2,3,i+1)
    plt.imshow(image[i],cmap = "gray")
    plt.title(title[i])
    plt.xticks([])
    plt.yticks([])

plt.show()