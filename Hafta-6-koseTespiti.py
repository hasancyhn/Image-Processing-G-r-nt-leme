import cv2
import numpy

imgColor = cv2.imread("ucgenDaire.jpg")
# Renk uzaylari arasinda donusum yapmak icin cv2.cvtColor() fonksiyonu kullanilir.
# Biz burada gri seviyeye donusturduk.
imgOrijinal = cv2.cvtColor(imgColor, cv2.COLOR_BGRA2GRAY)

imgFloat = numpy.float32(imgOrijinal)
# cv2.goodFeaturesToTrack() fonksiyonu ile ilk parametreyle kaynak goruntumuzu seceriz
# ikinci parametreyle istenilen kose sayisini belirtiriz.
# ucuncu parametre olarak kalite yuzdesini belirtiriz yani 0.01'İn uzerinde olanlari kose olarak degerlendir
# altindaysa kose statusune sokma demek isteniyor son parametreyle koseler arasi mesafeyi belirleriz.
kose = cv2.goodFeaturesToTrack(imgFloat, 20, 0.01, 10)
# Asagidaki len() fonksiyonu sayesinde 27 adet kosenin oldugunu ogrendık.
# Bir onceki satirda yer alan kodda 0.01 kalitesinde 20 adet kose istedik bize 27 kose arasindan bu ozelliklere sahip en iyi 20 koseyi getirecek.
print(len(kose))

for kose2 in kose:
    x, y = kose2.ravel()
    cv2.circle(imgColor, (int(x), int(y)), 2, (0, 255, 0), -1)

cv2.imshow("EKRAN-1", imgOrijinal)
cv2.imshow("EKRAN-2", imgColor)
cv2.waitKey(0)
cv2.destroyAllWindows()