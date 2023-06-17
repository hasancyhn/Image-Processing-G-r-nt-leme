from cv2 import cv2
import numpy

# Sahne Oluşturma
ekran = numpy.zeros((300, 300, 3), dtype=numpy.uint8) + 255
cv2.circle(ekran, (150, 150), 55, (30, 25, 255), 2)

cv2.imshow("EKRAN", ekran)
cv2.waitKey(0)
cv2.destroyAllWindows()