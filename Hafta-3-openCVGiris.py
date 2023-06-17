from cv2 import cv2
# PATH Olmadan Veri Okuma
imgRenkli = cv2.imread("yilan.jpg")
cv2.imshow("Hayvan", imgRenkli)

# Gri Olarak Resmi Goruntuleme
# imgGray = cv2.imread("yilan.jpg", cv2.IMREAD_GRAYSCALE)
# cv2.imshow("Hayvan", imgGray)

# PATH (Yol) Uzerinden Veri Okuma
# PATH uzerinden Turkce karakter ve bosluk olmamali
# imgPATH = cv2.imread("D:/DERSLER\NEÜ/3. Yıl Bahar Dönemi/Görüntü İşlemeye Giriş/kertenkele.jpg", cv2.IMREAD_GRAYSCALE)

cv2.namedWindow("Hayvan", cv2.WINDOW_NORMAL)
cv2.waitKey(0)
cv2.destroyAllWindows()