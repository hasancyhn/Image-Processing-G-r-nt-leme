import cv2
from matplotlib import pyplot, pyplot as plt

img1 = cv2.imread("img1.jpg")
img2 = cv2.imread("img2.jpg")

imgAnd = cv2.bitwise_and(img2, img1)
imgOr  = cv2.bitwise_or(img2, img1)
imgNot = cv2.bitwise_not(img2, img1)

cv2.imshow("img-1", img1)
cv2.imshow("img-2", img2)
cv2.imshow("imgAnd", imgAnd)
cv2.imshow("imgOr", imgOr)
cv2.imshow("imgNot", imgNot)

cv2.waitKey(0)
cv2.destroyAllWindows()
