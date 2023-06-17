import cv2
from matplotlib import pyplot, pyplot as plt

imgOrijinal = cv2.imread("particle.jpg", cv2.IMREAD_GRAYSCALE)
imgMean = cv2.blur(imgOrijinal, (10, 10))
imgMedian = cv2.medianBlur(imgOrijinal, 5)

cv2.imshow("EKRANIM-1", imgOrijinal)
cv2.imshow("EKRANIM-2", imgMean)
cv2.imshow("EKRANIM-3", imgMedian)
cv2.waitKey(0)
cv2.destroyAllWindows()
