#สร้างเส้นเชื่อมโยง
import cv2 
import numpy
img = numpy.zeros([600,600,3])

points = []

def clickPosition(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),10,(255,0,175),4)
        points.append((x,y))
        if len(points)>=2:
            cv2.line(img, points[0], points[1], (255,0,0), 5) 
            print(points)
            cv2.imshow("Output",img)
    
    cv2.imshow("Output",img)
    
    cv2.setMouseCallback("Output",clickPosition)
    cv2.waitKey(0)
    cv2.destroyAllWindows
    