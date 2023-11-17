import cv2

img = cv2.imread("image/V4.jpg")

eye = cv2.CascadeClassifier("dection/haarcascade_eye_tree_eyeglasses.xml")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
scaleFactor = 1.2
minNeighnber = 3
face = eye.detectMultiScale(gray,scaleFactor,minNeighnber)
for (x, y, w, h) in face:
    cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),thickness=6)