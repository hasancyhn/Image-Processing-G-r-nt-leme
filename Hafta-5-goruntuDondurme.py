import cv2
from matplotlib import pyplot, pyplot as plt

img = cv2.imread("kameraman.jpg", cv2.IMREAD_GRAYSCALE)
satir, sutun = img.shape

dondurmeSekli = cv2.getRotationMatrix2D((sutun/2, satir/2), 45, 1)
dondurulmuFotograf = cv2.warpAffine(img, dondurmeSekli, (sutun, satir))

cv2.imshow("EKRANIM-1", img)
cv2.imshow("EKRANIM-2", dondurulmuFotograf)

cv2.waitKey(0)
cv2.destroyAllWindows()
