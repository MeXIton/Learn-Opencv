import cv2 
import matplotlib.pyplot as plt 

img = cv2.imread("image/Coins.jpg",0)

Lapa = cv2.Laplacian(img,-1)

cv2.imshow("Original",img)
cv2.imshow("To Lapacian",Lapa)

cv2.waitKey(0)
cv2.destroyAllWindows()