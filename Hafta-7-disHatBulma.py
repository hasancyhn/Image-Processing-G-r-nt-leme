import cv2
import numpy

# Dis hat bulma ve cizme
imgOrijinal = cv2.imread("ikiKesikGoruntu.jpg")
# Goruntuyu once gri seviyeye daha sonra siyah beyaz seviyeye yani binary'ye ceviririz.
imgGray = cv2.cvtColor(imgOrijinal, cv2.COLOR_BGR2GRAY)
sonuc, imgEsik = cv2.threshold(imgGray, 125, 255, cv2.THRESH_BINARY)

cntrs, sonuc = cv2.findContours(imgEsik, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Koordinat degerleri
# print(len(cntrs))

cv2.drawContours(imgOrijinal, cntrs, -1, (0, 0, 255), 2)
cv2.imshow("EKRAN-1", imgOrijinal)
cv2.waitKey(0)
cv2.destroyAllWindows()