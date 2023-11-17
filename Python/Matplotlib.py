import cv2
from matplotlib import image
import matplotlib.pyplot as plt

gray_img = cv2.imread("image/V4.jpg")

thresh,result = cv2.threshold(gray_img, 128, 255, cv2.THRESH_BINARY)
thresh,result2 = cv2.threshold(gray_img, 128, 255, cv2.THRESH_BINARY_INV)
thresh,result3 = cv2.threshold(gray_img, 128, 255, cv2.THRESH_TRUNC)
thresh,result4 = cv2.threshold(gray_img, 128, 255, cv2.THRESH_TOZERO)
thresh,result5 = cv2.threshold(gray_img, 128, 255, cv2.THRESH_TOZERO_INV)
print(thresh)
#cv2.imshow("Original",gray_img)
#cv2.imshow("BINARY",result)
#cv2.imshow("BINARY_INV",result2)
#cv2.imshow("BINARY_INV",result3)
#cv2.imshow("BINARY_INV",result4)
#cv2.imshow("BINARY_INV",result5)
img = [gray_img,result,result2,result3,result4,result5]
title = ["Orignal","BINARY_INV","TRUNC","TOZENRO","TOZERO_INV"]

#for i in range(len(image)):
#    plt.subplot(2, 3, i+1)
 #   plt.imshow(image[i])
 #   plt.title(title[i])
 #   plt.xticks([]).plt.ytcks([])

#plt.show()