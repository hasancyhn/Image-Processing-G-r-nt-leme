import cv2
import numpy

def emptyFunction(x):
    pass

# Sahne Oluşturma
cv2.namedWindow("EKRAN")
cv2.createTrackbar("F-Size", "EKRAN", 55, 250, emptyFunction)

while True:
    ekran = numpy.zeros((512, 512, 3), dtype=numpy.uint8) + 255

cv2.waitKey(0)
cv2.destroyAllWindows()