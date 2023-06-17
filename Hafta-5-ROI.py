import cv2
from matplotlib import pyplot, pyplot as plt

img = cv2.imread("beyinTumoru.jpg")
print(img.shape)
# (249, 202, 3)
cv2.rectangle(img, (170, 160), (100, 90), (0, 255, 0), 3)

cv2.imshow("EKRANIM", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
