# แสดงวันและเวลาใน Video / กล้อง
import cv2
import datetime
cap = cv2.VideoCapture("Video/V2.mp4")

while (cap.isOpened):
   check , frame =  cap.read() #รับภาพจากกล้อง Fram ต่อ Fram
   
   if check == True :
    currentDate = str(datetime.datetime.now())
    cv2.putText(frame,currentDate,(10,30),cv2.FONT_HERSHEY_DUPLEX,0.8,(0,255,),cv2.LINE_4)
    cv2.imshow("Output", frame)
   
    if cv2.waitKey(1) &  0xFF == ord("e"):
        break
   
cap.release()
cv2.destroyAllWindows()