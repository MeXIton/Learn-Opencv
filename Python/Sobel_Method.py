import cv2 
import matplotlib.pyplot as plt 
import numpy as np

img = cv2.imread("image/Coins.jpg",0)


SobelX = cv2.Sobel(img,-1,1,0)
SobelY = cv2.Sobel(img,-1,0,1)
SobelXY = cv2.bitwise_or(SobelX,SobelY)


images = [img,SobelX,SobelY,SobelXY]
title = ["Original","SobelX","SobelY","SobelXY"]

for i in range(len(images)):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i],cmap="gray")   
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])
plt.show()

#cv2.imshow("Output",img)
#cv2.imshow("SobelX",SobelX)
#cv2.imshow("SobelY",SobelY)
#cv2.imshow("SObelXY",SobelXY)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
