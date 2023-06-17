import cv2
from matplotlib import pyplot, pyplot as plt

tom = cv2.imread("tom.jpg")
jerry = cv2.imread("jerry.jpg")
tomAndJerry = cv2.add(tom, jerry)

tomAndJerryWeighted = cv2.addWeighted(tom, 0.3, jerry, 0.7, 0)

cv2.imshow("EKRANIM", tomAndJerry)
cv2.waitKey(0)
cv2.destroyAllWindows()
