from cv2 import cv2
import numpy

# Sahne Oluşturma
ekran = numpy.zeros((300, 300, 3), dtype=numpy.uint8) + 255
x = (155, 50)
y = (100, 120)
z = (200, 150)

cv2.line(ekran, x, y, (0, 25, 155), 2)
cv2.line(ekran, y, z, (0, 25, 155), 2)
cv2.line(ekran, z, x, (0, 25, 155), 2)

cv2.imshow("EKRAN", ekran)
cv2.waitKey(0)
cv2.destroyAllWindows()