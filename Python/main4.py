#เปิดกล้องด้วย OpenCv

import cv2 

cap = cv2.VideoCapture(0)

while (True):
   check , frame =  cap.read() #รับภาพจากกล้อง Fram ต่อ Fram
   cv2.imshow("Out", frame)
   
   if cv2.waitKey(1) &  0xFF == ord("e"):
    break

cap.release()
cv2.destroyAllWindows
