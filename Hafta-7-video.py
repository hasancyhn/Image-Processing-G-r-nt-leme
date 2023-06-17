import cv2
import numpy

videomuz = cv2.VideoCapture("kopek.mp4")

while True:
    sonuc, frame = videomuz.read()
    if not sonuc:
        break

    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    low_limit = numpy.array([0, 0, 240])
    up_limit = numpy.array([255, 15, 255])

    frameMask = cv2.inRange(frameHSV, low_limit, up_limit)
    frameResult = cv2.bitwise_And(frame, frame, mask=frameMask)

    cv2.imshow("EKRAN-1", frame)
    cv2.imshow("EKRAN-2", frameResult)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

videomuz.release()
cv2.destroyAllWindows()
