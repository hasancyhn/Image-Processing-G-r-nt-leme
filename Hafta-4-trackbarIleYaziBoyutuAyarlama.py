from cv2 import cv2
import numpy

def emptyFunction(x):
    pass

# Sahne Oluşturma
cv2.namedWindow("EKRAN")
cv2.createTrackbar("F-Size", "EKRAN", 15, 100, emptyFunction)

fontBoyut = 0.25
while True:
    img = numpy.zeros((300, 300, 3), dtype=numpy.uint8) + 255
    cv2.putText(img, "OPEN-CV", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, fontBoyut, (0, 0, 255), cv2.LINE_4)
    cv2.imshow("EKRAN", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    fontBoyut = cv2.getTrackbarPos("F-Size", "EKRAN")
    fontBoyut = fontBoyut/100

cv2.destroyAllWindows()