import cv2

img = cv2.imread("image/V4.jpg")

# Read file Classification
face_cascade = cv2.CascadeClassifier("dection/haarcascade_frontalface_default.xml")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascade.detectMultiScale(gray)

scaleFactor = 1.1
minNeighner = 3 
face_detect = face_cascade.detectMultiScale(gray,scaleFactor,minNeighner)

for (x, y, w, h) in face_detect:
    cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),thickness=6)

cv2.imshow("Output",face_cascade)
cv2.waitKey(0) 
cv2.destroyAllWindows()