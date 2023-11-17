import cv2

#  อ่านภาพ 
img = cv2.imread("image/Pic4.png")

# กําหนดขนาด 
imgresize = cv2.resize(img,(1000,750))


# วาดสี่เหลี่ยม
# rectangle (ภาพ ,  มุมที่1  , (บนซ้าย),มุมที่2 (ล่างขวา)ม สี (BGR), ความหนา)

cv2.rectangle(imgresize,(100,100),(500,500),(255,0,255),-1)
cv2.rectangle(imgresize,(100,100),(500,500),(255,255,255),20)
cv2.imshow("Output",imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()