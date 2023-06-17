import cv2
from matplotlib import pyplot, pyplot as plt

img = cv2.imread("kameraman.jpg")

plt.hist(img.ravel(), 256, [0, 200])
plt.show()
