import cv2
pipeline = "rtspsrc location=\"rtsp://login:password@host:port/\" ! rtph264depay ! h264parse ! omxh264dec ! nvvidconv ! video/x-raw, format=(string)BGRx! videoconvert ! appsink"
capture = cv2.VideoCapture(0, cv2.CAP_V4L)
count = 0 
while capture.isOpened():
    print("hello", count)
    count += 1
    res, frame = capture.read()
    cv2.imshow("Video", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
capture.release()
cv2.destroyAllWindows()