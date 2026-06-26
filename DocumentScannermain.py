import cv2
import numpy as np
import utils


webCamFeed = True
pathImage = "a.jpg"
cap = cv2.VideoCapture(1)
cap.set(10, 160)
heightImg = 640
widthImg = 480


utils.initializeTrackbars()
count = 0


while True:

    imgBlank = np.zeros((heightImg, widthImg, 3), np.uint8)

    if webCamFeed:success, img = cap.read()
    else:img = cv2.imread(pathImage)
    img = cv2.resize(img, (widthImg, heightImg))