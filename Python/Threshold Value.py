import cv2 
import Matplotlib.pyplot as plt

gray_img = cv2.imread("image/V4.jpg")
gray_img1 = cv2.cvtColor(cv2.COLOR_BGR2GRAY)

thresh_value = [50,100,130,200,230]
plt.subplot(231,xticks = [], yticks = [])
plt.title("Original")
plt.imshow(gray_img,camp = "gray")

for i in range(len(thresh_value)):
    thresh,result = cv2.threshold(gray_img,thresh_value[i],255,cv2.THRESH_BINARY)
    plt.subplot(232+i)
    plt.title("%d"%thresh_value[i])
    plt.show(result,cmap = 'gray')
    plt.xticks([]),plt.ytricks([])
