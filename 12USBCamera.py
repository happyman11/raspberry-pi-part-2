import cv2
cam = cv2.VideoCapture(2)

while True:
        _,img = cam.read()
        cv2.imshow("VideoStream", img)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
                break
cam.release()
cv2.destroyAllWindows()
