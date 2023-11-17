import cv2 
Video = cv2.VideoCapture("Video/V3.mp4")

face_cascade = cv2.CascadeClassifier("dection/haarcascade_frontalface_default.xml")

while (Video.isOpened()):
    check , fram = Video.read()
    if check == True:
        gray = cv2.cvtColor(fram,cv2.COLOR_BGR2GRAY)
        scaleFactor = 1.1
        minNeighner = 3
        face_detect = face_cascade.detectMultiScale(gray,scaleFactor,minNeighner)
        for (x, y, w, h) in face_detect:
            cv2.rectangle(fram, (x,y),(x+w,y+h),(0,255,0),thickness=6)

        cv2.imshow("OutputVideo",fram)
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else:
        break

Video.release()
cv2.destroyAllWindows()