import cv2
import numpy as np
from pyzbar.pyzbar import decode

#img = cv2.imread("pic2.png")

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

with open('Database.text') as file:
    lists=file.read().splitlines()

while True:
    success,img=cap.read()

    for i in decode(img):
        data=i.data.decode("utf-8")
        print(data)

        # Creating boundary box
        points=np.array([i.polygon],np.int32)
        points=points.reshape((-1,1,2))
        if data in lists:
            print("Authorized")
            cv2.polylines(img, [points], True, (0, 255, 0), 4)
            TopPoints = i.rect
            cv2.putText(img, "Accepted", (TopPoints[0], TopPoints[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 3)
        else:
            print("Un-Authorized")
            cv2.polylines(img, [points], True, (0, 0, 255), 4)
            TopPoints = i.rect
            cv2.putText(img, "Not Accepted", (TopPoints[0], TopPoints[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255),
                        3)
        # Putting text
        # TopPoints=i.rect
        # cv2.putText(img,data,(TopPoints[0],TopPoints[1]),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),3)

    cv2.imshow("Output",img)
    cv2.waitKey(1)
