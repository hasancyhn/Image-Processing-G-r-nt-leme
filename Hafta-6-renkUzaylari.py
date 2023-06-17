import cv2
from matplotlib import pyplot, pyplot as plt

imgOrijinal = cv2.imread("yilan.jpg")

imgGray = cv2.cvtColor(imgOrijinal, cv2.COLOR_BGR2GRAY)
imgHSV = cv2.cvtColor(imgOrijinal, cv2.COLOR_BGR2HSV)

# cv2.imshow("EKRAN-1", imgOrijinal)
# cv2.imshow("EKRAN-2", imgGray)
# cv2.imshow("EKRAN-3", imgHSV)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Hafta-7 dakika 25
plt.subplot(131), plt.imshow(imgOrijinal, cmap='gray'), plt.title("Orijinal"), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(imgGray, cmap='gray'), plt.title("Gray")
plt.subplot(133), plt.imshow(imgHSV, cmap='gray'), plt.title("HSV")
plt.show()