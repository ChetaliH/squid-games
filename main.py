#INITIAL SETUP
#----------------------------------------------------------------
import cv2
from cvzone import HandTrackingModule, overlayPNG
import numpy as np
intro =cv2.imread('img1.jpeg')# read frames\img 1 in the intro variable
kill =cv2.imread('img2.png')# read frames\img 2 in the kill variable
winner =cv2.imread('img3.png') # read frames\img 3 in the winner variable
cam =cv2.VideoCapture(0)
while True:
    isTrue,frame=cam.read()
    cv2.imshow('Video',frame)
    if(cv.waitKey(1000) & 0xFF==ord(x)):
        break#read the camera
detector = HandTrackingModule.HandDetector(maxHands=1,detectionCon=0.77)
#sets the minimum confidence threshold for the detection

#INITILIZING GAME COMPONENTS
#----------------------------------------------------------------
sqr_img = cv2.imread('sqr(2).png')# read img\sqr (1) in the sqr_img variable
mlsa = cv2.imread('mlsa.png')  # read img\mlsa in the mlsa variable
cv2.imshow('squid game',cv2.resize(intro,(0,0),fx=0.69,fy=0.69))
cv2.waitkey(1000)

while True:
    cv2.imshow('squid game',cv2.resize(intro,(0,0),fx=0.69,fy=0.69))
    if cv2.waitkey(1000) & 0xFF==ord('q'):
        break#INTRO SCREEN WILL STAY UNTIL Q IS PRESSED
gameOver = False
NotWon =True
#GAME LOGIC UPTO THE TEAMS
cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
while True:
    success, image = cap.read()
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(imageRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks: # working with each hand
            for id, lm in enumerate(handLms.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
    if id == 20 :

        cv2.circle(image, (cx, cy), 25, (255, 0, 255), cv2.FILLED)

        mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)
        cv2.imshow("Output", image)
        cv2.waitKey(1)
#-----------------------------------------------------------------------------------------
while not gameOver:
        continue
#LOSS SCREEN
if NotWon:
    for i in range(10):
       cv2.imshow('game over',kill)#show the loss screen from the kill image read before
    while True:
        cv2.imshow('squid game',cv2.resize(kill,(0,0),fx=0.69,fy=0.69))
        if cv2.waitkey(1000) & 0xFF==ord('q'):
            break#show the loss screen from the kill image read before and end it after we press q

else:
    cv2.imshow('winner',winner)
#WIN SCREEN
#show the win screen from the winner image read before

    while True:
        cv2.imshow('squid game',cv2.resize(winner,(0,0),fx=0.69,fy=0.69))
        if cv2.waitkey(1000) & 0xFF==ord('q'):
            break

        #show the win screen from the winner image read before and end it after we press q

capture.release()
cv2.destroyAllWindows()

        

#destroy all the windows

