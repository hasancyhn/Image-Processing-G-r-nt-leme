from cv2 import cv2
import numpy

# Sahne Oluşturma
ekran = numpy.zeros((300, 300, 3), dtype=numpy.uint8) + 255

noktalar = numpy.array([[50, 100], [75, 100], [125, 175], [75, 200]], numpy.int32)
cv2.polylines(ekran, [noktalar], False, (125, 125, 125), 2)

cv2.imshow("EKRAN", ekran)
cv2.waitKey(0)
cv2.destroyAllWindows()