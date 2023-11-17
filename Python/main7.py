import cv2

#  อ่านภาพ 
img = cv2.imread("image/Pic4.png")

# กําหนดขนาด 
imgresize = cv2.resize(img,(1000,750))


# วาดเส้นตรง 
# line (ภาพ ,  จุดเริ่มต้น (x,y) , จุดสุดท้าย (x,y), สี (BGR), ความหนา)

cv2.arrowedLine(imgresize, (0,0), (100,100), (255,0,255),20)
cv2.line(imgresize, (0,0), (100,550), (255,255,255),20)
cv2.imshow("Output",imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()