import cv2
import numpy

imgOrijinal = cv2.imread("ikiKesikGoruntu.jpg")
imgGray = cv2.cvtColor(imgOrijinal, cv2.COLOR_BGR2GRAY)
sonuc, imgEsik = cv2.threshold(imgGray, 125, 255, cv2.THRESH_BINARY)
cntrs, sonuc = cv2.findContours(imgEsik, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imgOrijinal, cntrs, -1, (0, 0, 255), 2)

cntr = cntrs[2]
mmnts = cv2.moments(cntr)

centerX = int(mmnts["m10"]/mmnts["m00"])
centerY = int(mmnts["m01"]/mmnts["m00"])
cv2.circle(imgOrijinal, (centerY, centerY), 3, (255, 0, 0), -1)
cv2.imshow("EKRAN-1", imgOrijinal)
cv2.waitKey(0)
cv2.destroyAllWindows()
