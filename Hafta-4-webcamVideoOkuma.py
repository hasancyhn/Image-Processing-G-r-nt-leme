from cv2 import cv2

"""
# Webcam'den Video Okuma
goruntu = cv2.VideoCapture(0)
while True:
    state, goruntum = goruntu.read()
    goruntum = cv2.flip(goruntum, 1)
    cv2.imshow("Kameram", goruntum)
    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

goruntu.release()
cv2.destroyAllWindows()
"""

# Kaydedilmiş (Hazır) Video Okuma
video1 = cv2.VideoCapture("malaysia.mp4")
while True:
    state, videom = video1.read()
    if state == 0:
        break
    videom =cv2.resize(video1, (480, 480))
    cv2.imshow("Malezya Videosu", videom)
    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

video1.release()
cv2.destroyAllWindows()