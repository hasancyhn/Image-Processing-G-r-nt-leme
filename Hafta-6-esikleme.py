import cv2

imgOrijinal = cv2.imread("kameraman.jpg")
sonuc, imgEsikBinary = cv2.threshold(imgOrijinal, 125, 255, cv2.THRESH_BINARY)
# sonuc, imgEsikOtsu = cv2.threshold(imgOrijinal, 125, 255, cv2.THRESH_OTSU)

cv2.imshow("EKRAN-1", imgOrijinal)
cv2.imshow("EKRAN-2", imgEsikBinary)
# cv2.imshow("EKRAN-3", imgEsikOtsu)
cv2.waitKey(0)
cv2.destroyAllWindows()