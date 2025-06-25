import cv2
import numpy as np
green = np.uint8([[[0, 255, 0]]])
hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
green_lower = np.uint8([hsv_green[0, 0, 0]-25, 100, 100])
green_upper = np.uint8([hsv_green[0, 0, 0]+25, 255, 255])
capture = cv2.VideoCapture('ball_detect.mp4')
while True:
    isTrue, frame = capture.read()
    if not isTrue:
        break
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv_frame = cv2.GaussianBlur(hsv_frame, (9, 9), cv2.BORDER_DEFAULT)
    hsv_frame = cv2.erode(hsv_frame, None, iterations = 5)
    hsv_frame = cv2.dilate(hsv_frame, None, iterations = 5)
    mask = cv2.inRange(hsv_frame, green_lower, green_upper)
    contours, hierarchies = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
        c = max(contours, key = cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        cv2.circle(frame, (int(x), int(y)), int(radius), (0, 0, 255), 2)
    cv2.imshow('Video', frame)
    if cv2.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv2.destroyAllWindows()