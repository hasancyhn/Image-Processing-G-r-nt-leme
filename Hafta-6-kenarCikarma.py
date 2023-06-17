import cv2
import numpy

imgOrijinal = cv2.imread("kameraman.jpg")
#Kenar dedigimiz beyaz cizgilerdir.
kenarlariCikarilmisGoruntu = cv2.Canny(imgOrijinal, 50, 150)

cv2.imshow("EKRAN-1", imgOrijinal)
cv2.imshow("EKRAN-2", kenarlariCikarilmisGoruntu)
cv2.waitKey(0)
cv2.destroyAllWindows()