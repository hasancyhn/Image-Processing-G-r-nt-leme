import cv2
from matplotlib import pyplot, pyplot as plt

fotograf = cv2.imread("kameraman.jpg")
toplanmisGoruntu = cv2.add(fotograf, 50)
cikarilmisGoruntu = cv2.add(fotograf, -50)

cv2.imshow("Orijinal Goruntu", fotograf)
cv2.imshow("Toplanmis Goruntu", toplanmisGoruntu)
cv2.imshow("Cikarilmis Goruntu", cikarilmisGoruntu)

cv2.waitKey(0)
cv2.destroyAllWindows()
