import cv2 
import matplotlib.pyplot as plt

img = cv2.imread("image/MAP.jpg",0)


thresh, result = cv2.threshold(img,128,255,cv2.THRESH_BINARY)
# Box Size
size = [3,5,9,17,33]
plt.subplot(231, xtrick = [], ytrick = [])
plt.imshow(img,cmap = "gray")
plt.show()

for i in range(len(size)):
   result =  th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,size [i],1)
   plt.subplot(232+i)
   plt.title("%d"%size[i])
   plt.imshow(result,cmap = "gray")
   plt.xtrick([]),plt.ytricks([])