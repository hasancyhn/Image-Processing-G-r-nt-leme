from cv2 import cv2
import numpy

# Sahne Oluşturma
ekran = numpy.zeros((300, 300, 3), dtype=numpy.uint8) + 255
cv2.rectangle(ekran, (50, 50), (10, 25), (255, 0, 0), 2)
cv2.rectangle(ekran, (75, 75), (100, 100), (0, 0, 255), -1)

cv2.imshow("EKRAN", ekran)
cv2.waitKey(0)
cv2.destroyAllWindows()