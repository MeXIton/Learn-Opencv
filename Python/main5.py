# เปิด Video ด้วย Opencv

import cv2 

cap = cv2.VideoCapture("Video/V2.mp4")

while (cap.isOpened):
   check , frame =  cap.read() #รับภาพจากกล้อง Fram ต่อ Fram
   
   if check == True :
    gray  = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
    cv2.imshow("Out", gray)
   
    if cv2.waitKey(1) &  0xFF == ord("e"):
        break
    else: 
        break
cap.release()
cv2.destroyAllWindows()