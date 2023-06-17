import cv2
import numpy

imgOrijinal = cv2.imread("ikiKesikGoruntu.jpg")
imgGray = cv2.cvtColor(imgOrijinal, cv2.COLOR_BGR2GRAY)
sonuc, imgEsik = cv2.threshold(imgGray, 125, 255, cv2.THRESH_BINARY)
cntrs, sonuc = cv2.findContours(imgEsik, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imgOrijinal, cntrs, -1, (0, 0, 255), 2)

cntr = cntrs[0]
mmnts = cv2.moments(cntr)
# Dictionary yani sozluk yapisini elde ederiz.
# print("Moments", mmnts)
area = mmnts["m00"]
print("Area with moment: ", area)

area = cv2.contourArea(cntr)
print("Area with CV2: ", area)

cv2.imshow("EKRAN-1", imgOrijinal)
cv2.waitKey(0)
cv2.destroyAllWindows()