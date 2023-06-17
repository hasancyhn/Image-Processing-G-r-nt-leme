import cv2
import numpy

imgOrijinal = cv2.imread("particle.jpg", cv2.IMREAD_GRAYSCALE)
imgTersi = cv2.bitwise_not(imgOrijinal)

# 1'ler olusan 5'e 5'lik bir matrix olusturalim.
maske = numpy.ones((2,2), numpy.uint8)

# iterations: Resmin kac kere asinacagini belirtir.
imgAsindirma = cv2.erode(imgOrijinal, maske, iterations=1)
imgDilated = cv2.dilate(imgOrijinal, maske, iterations=1)
imgOpened = cv2.morphologyEx(imgOrijinal, cv2.MORPH_OPEN, maske)
imgClosed = cv2.morphologyEx(imgOrijinal, cv2.MORPH_CLOSE, maske)

cv2.imshow("ORIJINAL", imgOrijinal)
cv2.imshow("ASINDIRMA", imgAsindirma)
cv2.imshow("GENISLETILMIS", imgDilated)
cv2.imshow("ACMA", imgOpened)
cv2.imshow("KAPAMA", imgClosed)
cv2.waitKey(0)
cv2.destroyAllWindows()