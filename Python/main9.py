import cv2

#  อ่านภาพ 
img = cv2.imread("image/Pic4.png")

# กําหนดขนาด 
imgresize = cv2.resize(img,(1000,750))


# วาดสี่เหลี่ยม
# circle (ภาพ , ตําแหน่งจุดศูนย์กลางวงกลม (x,y), รัศมี, สี (BGR), ความหนา)
cv2.circle(imgresize,(550,250),180,(180,0,255),8)
cv2.imshow("Output",imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()