import cv2

img = cv2.imread("yilan.jpg")
print(img)

dim = img.shape
print(dim)
# (345, 460, 3)

pixel1 = img[250, 250, 1]
print(pixel1)
# 138

pixel2 = img[:, :, 0]
print(pixel2)
# [[  6   6   6 ...   4   4   4]
#  [  6   6   6 ...   4   4   4]
#  [  6   6   6 ...   4   4   4]
#  ...
#  [ 44  47  53 ... 112 118 118]
#  [ 50  53  59 ... 129 123 110]
#  [ 57  60  65 ... 108 105 113]]