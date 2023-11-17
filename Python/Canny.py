import cv2
import matplotlib.pyplot as plt 

img = cv2.imread("image/Coins.jpg")

Canny  = cv2.Canny(img,50,200)

cv2.imshow("Original",img)
cv2.imshow("To Canny",Canny)

cv2.waitKey(0)
cv2.destroyAllWindows()
