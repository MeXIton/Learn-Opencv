import cv2 
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image/MAP.jpg",0)
kernel = np.ones((6,6),np.float32)/6
#Filter2D
convolution = cv2.filter2D(img,-1,kernel)

#BLUR
blur = cv2.blur(img,(5,5))

#Median
MD = cv2.medianBlur(img,5)


GU = cv2.GaussianBlur(img,(5,5),0)


title = ["ORIGINAL","CONVOLUTION 3x3","BLUR","MD","GU"]
image = [img,convolution,blur,MD,GU]

for i in range(len(image)):
    plt.subplot(2,3,i+1)
    plt.imshow(image[i])
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])

plt.imshow(img)
plt.show()
