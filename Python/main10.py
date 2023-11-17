import cv2

#  อ่านภาพ 
img = cv2.imread("image/Pic4.png")

# กําหนดขนาด 
imgresize = cv2.resize(img,(1000,750))


# วาดสี่เหลี่ยม
# putText (ภาพ ,  ข้อความ  , พิกัดที่จะแสดง (x,y),font, ขนาดข้อความ,  สี (BGR), ความหนา)
cv2.putText(imgresize, "I kuy Plume", (450,250),cv2.FONT_HERSHEY_SIMPLEX,1,(0,190,220),cv2.LINE_4)
cv2.imshow("Output",imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()