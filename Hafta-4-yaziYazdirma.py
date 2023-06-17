import cv2
import numpy

# Sahne Oluşturma
ekran = numpy.zeros((300, 300, 3), dtype=numpy.uint8) + 255

cv2.putText(ekran, "Goruntu Isleme", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.95, (0, 0, 255), cv2.LINE_4)

cv2.imshow("EKRAN", ekran)
cv2.waitKey(0)
cv2.destroyAllWindows()