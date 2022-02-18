import cv2
import numpy as np
import autopy
import time
import mediapipe as mp
import math
from basic import frame
from tkinter import *

def virtual_mouse():
    ####################################################
    wScr, hScr = autopy.screen.size()
    # print (wScr,hScr)
    scale = 0.8
    pTime = 0
    cap = cv2.VideoCapture(0)
    cap.set(3, wScr*scale)
    cap.set(4, hScr*scale)
    frameR = 100  # Frame Reduction
    smoothening = 7
    plocX,plocY = 0,0
    clocX,clocY = 0,0
    ###################################################
    mpHands = mp.solutions.hands
    hands = mpHands.Hands()
    tipIds = [4, 8, 12, 16, 20]


    while True:
        wait=1
        #############################################################
        # 1. Find hand Landmarks
        success, img = cap.read()
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)
        # print(results.multi_hand_landmarks)

        handNo = 0
        draw = True
        xList = []
        yList = []
        bbox = []
        lmList = []
        if results.multi_hand_landmarks:
            Label(bg="yellow").place(relx=0.95,rely=0.03,relheight=0.03,relwidth=0.03)
            #########################  Finding largest hands  #####################
            best = [0, 0]
            for i in range(len(results.multi_hand_landmarks)):
                tx, ty, bx, by = 0, 0, 0, 0
                for Id, lm in enumerate(results.multi_hand_landmarks[i].landmark):
                    if (Id == 12):
                        tx, ty = lm.x, lm.y
                    if (Id == 0):
                        bx, by = lm.x, lm.y

                temp = math.hypot(tx - bx, ty - by)
                if temp > best[1]:
                    best[0] = i
                    best[1] = temp

            myHand = results.multi_hand_landmarks[best[0]]
            for Id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                xList.append(cx)
                yList.append(cy)
                # print(id, cx, cy)
                lmList.append([Id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

            xMin, xMax = min(xList), max(xList)
            yMin, yMax = min(yList), max(yList)
            bbox = xMin, yMin, xMax, yMax
            if draw:
                cv2.rectangle(img, (xMin - 20, yMin - 20), (xMax + 20, yMax + 20), (0, 255, 0), 2)

        else:
            Label(bg="red").place(relx=0.95,rely=0.03,relheight=0.03,relwidth=0.03)            

        ####################################################################################
        # 2.Check fingers are up
        if len(lmList) != 0:           
            x1, y1 = lmList[8][1:]
            x2, y2 = lmList[12][1:]
            # print(x1,y1,x2,y2)
            #####################################################################################
            # 3. Check which fingers are up

            fingers = []
            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # other four fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            # print(fingers)

            cv2.rectangle(img, (frameR, 10), (int(wScr*scale)-frameR, int(hScr/2.20)), (255, 0, 255), 2)

    ################################################################################
            # 4. Only Index Finger : Moving Mode
            if fingers[1] == 1 and fingers[2] == 0:
                Label(bg="green").place(relx=0.95,rely=0.03,relheight=0.03,relwidth=0.03)
                # 5. Convert Coordinates
                if (x1 <= frameR):
                    x1 = frameR+5
                if (x1 >= int(wScr*scale) - frameR):
                    x1 = int(wScr*scale) - frameR-5
                if (y1 <= 10):
                    y1 = 10+5
                if (y1 >= int(hScr/2.2)):
                    y1 = int(hScr/2.2)-5
                x3 = np.interp(x1, (frameR, int(wScr*scale) - frameR), (0, wScr))
                y3 = np.interp(y1, (10, int(hScr/2.2)), (0, hScr))
                #print(x3,y3)

                # 6. Smoothen Values
                clocX = plocX + (x3 - plocX) / smoothening
                clocY = plocY + (y3 - plocY) / smoothening

                # 7. Move mouse
                #autopy.mouse.move(wScr-x3,y3)
                autopy.mouse.move(wScr - clocX, clocY)
                cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
                plocX, plocY = clocX, clocY

    ################################################################################
            # 8. Both Index and middle fingers are up : Clicking Mode
            if fingers[1] == 1 and fingers[2] == 1:

                # 9. Find distance between fingers
                dist=0
                p1,p2=8,12
                xa, ya = lmList[p1][1:]
                xb, yb = lmList[p2][1:]
                ca, cb = (xa + xb) // 2, (ya + yb) // 2
                if draw:
                    cv2.line(img, (xa, ya), (xb, yb), (255, 0, 255), 3)
                    cv2.circle(img, (xa, ya), 15, (255, 0, 255), cv2.FILLED)
                    cv2.circle(img, (xb, yb), 15, (255, 0, 255), cv2.FILLED)
                    cv2.circle(img, (ca, cb), 15, (0, 0, 255), cv2.FILLED)
                    dist = math.hypot(xa - xb, ya - yb)

                #print(dist)
                # 10.click mouse if distance short
                if dist < 30 :
                    wait=250
                    Label(bg="green").place(relx=0.95,rely=0.03,relheight=0.03,relwidth=0.03)
                    cv2.circle(img, (ca, cb), 15, (0, 255, 0), cv2.FILLED)
                    autopy.mouse.click()
                    

    #################################################################################
        # 11. Frame Rate
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(wait)