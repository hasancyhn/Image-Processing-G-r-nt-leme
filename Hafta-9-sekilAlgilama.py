import cv2
import numpy

img = cv2.imread("sekiller.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
res, imgThresh = cv2.threshold(imgGray, 125, 255, cv2.THRESH_BINARY)

cntrs, res = cv2.findContours(imgThresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cntr in cntrs:
    print("Contor: ", len(cntr))
    hassasiyet = 0.01*cv2.arcLength(cntr, True)
    cerceve = cv2.approxPolyDP(cntr, hassasiyet,True)
    print("Cerceve: ", len(cerceve))

    cv2.drawContours(img, [cerceve], 0, (0, 255, 0), 3)

    sekilIsmi = ""
    if len(sekilIsmi) == 3:
        shapeName = "UCGEN"
    elif len(cerceve) == 4:
        sekilIsmi = "DORTGEN"
    elif len(cerceve) == 5:
        sekilIsmi = "BESGEN"
    else:
        sekilIsmi = "COKGEN"

    print(cerceve)
    x = cerceve.ravel()[0]
    y = cerceve.ravel()[1]

    cv2.putText(img, sekilIsmi, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))

cv2.imshow("SEKIL", img)
cv2.waitKey(0)
cv2.destroyAllWindows()