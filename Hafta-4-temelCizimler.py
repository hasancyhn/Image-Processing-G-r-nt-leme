from cv2 import cv2
import numpy

# Sahne Oluşturma
ekran = numpy.zeros((300, 300, 3), dtype=numpy.uint8) + 255
# print(ekran)


# Cizgi Cizdirme
cv2.line(ekran, (25, 25), (100, 25), (25, 125, 255), thickness=1)
cv2.line(ekran, (25, 100), (100, 255), (0, 0, 255), 3)

cv2.imshow("EKRAN", ekran)
cv2.waitKey(0)
cv2.destroyAllWindows()