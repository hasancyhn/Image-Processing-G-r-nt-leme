import cv2
import numpy

video1 = cv2.VideoCapture("trafik.mp4")
res, anaVideo = video1.read()
anaVideo = cv2.resize(anaVideo, (640, 480))
anaVideoGray = cv2.cvtColor(anaVideo, cv2.COLOR_BGR2GRAY)

while True:
    res, videom = video1.read()
    if not res:
        break


    videom = cv2.resize(videom, (640, 480))
    griVideo = cv2.cvtColor(videom, cv2.COLOR_BGR2GRAY)
    griVideoFarki = cv2.absdiff(anaVideoGray, griVideo)
    res, griVideoFarkiBinary = cv2.threshold(griVideoFarki, 50, 255, cv2.THRESH_BINARY)

    cv2.imshow("Orijinal Trafik Videosu", videom)
    cv2.imshow("Gri Trafik Videosu", griVideoFarki)
    cv2.imshow("Gri Trafik Videosu Binary", griVideoFarkiBinary)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

video1.release()
cv2.destroyAllWindows()
video1 = cv2.VideoCapture("trafik.mp4")
res, anaVideo = video1.read()
anaVideo = cv2.resize(anaVideo, (640, 480))
anaVideoGray = cv2.cvtColor(anaVideo, cv2.COLOR_BGR2GRAY)

while True:
    res, videom = video1.read()
    if not res:
        break


    videom = cv2.resize(videom, (640, 480))
    griVideo = cv2.cvtColor(videom, cv2.COLOR_BGR2GRAY)
    griVideoFarki = cv2.absdiff(anaVideoGray, griVideo)
    res, griVideoFarkiBinary = cv2.threshold(griVideoFarki, 50, 255, cv2.THRESH_BINARY)

    cv2.imshow("Orijinal Trafik Videosu", videom)
    cv2.imshow("Gri Trafik Videosu", griVideoFarki)
    cv2.imshow("Gri Trafik Videosu Binary", griVideoFarkiBinary)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

video1.release()
cv2.destroyAllWindows()

"""
video1 = cv2.VideoCapture("trafik.mp4")
ayracMaske = cv2.createBackgroundSubtractorM0G2(history = 50, varThresold = 50, detectShadows = True)

while True:
    res, videom = video1.read()
    if not res:
        break

    videom = cv2.resize(videom, (640, 480))
    videoFark = ayracMaske.apply(videom)

    cv2.imshow("Orijinal Trafik Videosu", videom)
    cv2.imshow("Trafik Videosu Farki", videoFark)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

video1.release()
cv2.destroyAllWindows()
"""