import cv2 
import matplotlib.pyplot as plt 

img = cv2.imread("/image/MAP.jpg",0)

thresh, make = cv2.threshold(img,170,255,cv2.THRESH_BINARY_INV)
title = ["ORIGINAL","THRESH"]
image = [img,make]

for i in range(len(img)):
    plt.subplot(1,2,i+1)
    plt.imshow(image[i],cmap = "gray")
    plt.title(title[i])
    plt.xtrick([])
    plt.ytrick([])

plt.show()

