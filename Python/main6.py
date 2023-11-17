# การอัด Video
import cv2 

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XIVD')

result = cv2.VideoWriter("Output.avi",fourcc, 20, (640,480))

while (cap.isOpened):
   check , frame =  cap.read() #รับภาพจากกล้อง Fram ต่อ Fram
   
   if check == True :
    cv2.imshow("Out",frame)
    result.write(frame)
    if cv2.waitKey(0) &  0xFF == ord("e"):
        break
    else :
        break
    
result.release()
cap.release()
cv2.destroyAllWindows
