# อ่านภาพ
import cv2 

img =  cv2.imread("image/Pic1.png")
cv2.imshow("Output",img)
cv2.waitKey(delay=0)
cv2.destroyAllWindows
print(img)
print(type(img.ndim))


