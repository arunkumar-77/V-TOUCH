import cv2
import numpy as np
import autopy
import time
import mediapipe as mp
import math
from basic import frame
from tkinter import *

from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import os



def detect_and_predict_mask(r_img, faceNet, maskNet):
    # grab the dimensions of the r_img and then construct a blob
    # from it
    (h, w) = r_img.shape[:2]
    blob = cv2.dnn.blobFromImage(r_img, 1.0, (224, 224),
                                 (104.0, 177.0, 123.0))

    # pass the blob through the network and obtain the face detections
    faceNet.setInput(blob)
    detections = faceNet.forward()
    #print(detections.shape)

    # initialize our list of faces, their corresponding locations,
    # and the list of predictions from our face mask network
    faces = []
    locs = []
    preds = []

    # loop over the detections
    for i in range(0, detections.shape[2]):
        # extract the confidence (i.e., probability) associated with
        # the detection
        confidence = detections[0, 0, i, 2]

        # filter out weak detections by ensuring the confidence is
        # greater than the minimum confidence
        if confidence > 0.5:
            # compute the (x, y)-coordinates of the bounding box for
            # the object
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            # ensure the bounding boxes fall within the dimensions of
            # the r_img
            (startX, startY) = (max(0, startX), max(0, startY))
            (endX, endY) = (min(w - 1, endX), min(h - 1, endY))

            # extract the face ROI, convert it from BGR to RGB channel
            # ordering, resize it to 224x224, and preprocess it
            face = r_img[startY:endY, startX:endX]
            face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
            face = cv2.resize(face, (224, 224))
            face = img_to_array(face)
            face = preprocess_input(face)

            # add the face and bounding boxes to their respective
            # lists
            faces.append(face)
            locs.append((startX, startY, endX, endY))

    # only make a predictions if at least one face was detected
    if len(faces) > 0:
        # for faster inference we'll make batch predictions on *all*
        # faces at the same time rather than one-by-one predictions
        # in the above `for` loop
        faces = np.array(faces, dtype="float32")
        preds = maskNet.predict(faces, batch_size=32)

    # return a 2-tuple of the face locations and their corresponding
    # locations
    
    ## loop over the detected face locations and their corresponding
        # locations to get largest face
    min_area=0
    box=()
    pred=()
    for (b, p) in zip(locs, preds):            
        (startX, startY, endX, endY) = b
        x = endX-startX
        y = endY-startY
        if(x*y > min_area):
            min_area = x*y
            box=b
            pred=list(p)

    return pred
       
def camera1():
    print("Session Details")
    ##VIRTUAL MOUSE
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
    mpHands = mp.solutions.hands
    hands = mpHands.Hands()
    tipIds = [4, 8, 12, 16, 20]
    ###################################################

    ##MASK DETECTION
    ###################################################

    label= Label(text= "WEAR YOUR MASK \nTO CONTINUE TRANSACTION", font= ('Helvetica bold', 70))
    prototxtPath = r"C:\Users\91638\OneDrive\Documents\GitHub\V-TOUCH\Mask_detection\face_detector\deploy.prototxt"
    weightsPath = r"C:\Users\91638\OneDrive\Documents\GitHub\V-TOUCH\Mask_detection\face_detector\res10_300x300_ssd_iter_140000.caffemodel"
    faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)

    # # load the face mask detector model from disk
    maskNet = load_model(r"C:\Users\91638\OneDrive\Documents\GitHub\V-TOUCH\Mask_detection\mask_detector.model")

    i=0
    no = 0
    flag = 0 ##mask
    info=""
    color=(0, 0, 255)

    while True:
        wait=1
        success, img = cap.read()

        ##VIRSTUAL MOUSE
        #############################################################
        # 1. Find hand Landmarks
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
            for j in range(len(results.multi_hand_landmarks)):
                tx, ty, bx, by = 0, 0, 0, 0
                for Id, lm in enumerate(results.multi_hand_landmarks[j].landmark):
                    if (Id == 12):
                        tx, ty = lm.x, lm.y
                    if (Id == 0):
                        bx, by = lm.x, lm.y

                temp = math.hypot(tx - bx, ty - by)
                if temp > best[1]:
                    best[0] = j
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
            if (fingers[1] == 1 and fingers[2] == 0) or (fingers[1] == 1 and fingers[2] == 0):
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
                    

        ###############################################################################
        ###MASK DETECTION
        if(i%5==0):
            r_img = cv2.resize(img,(400,400))
            pred = detect_and_predict_mask(r_img, faceNet, maskNet)
            if pred:
                ans = 0 if pred[0]>pred[1] else 1            ##  0->mask  and  1->no mask
                no+=ans

                (mask, withoutMask) = pred
                # determine the class label and color we'll use to draw
                # the bounding box and text
                info = "Mask" if mask > withoutMask else "No Mask"
                color = (0, 255, 0) if info == "Mask" else (0, 0, 255)

                # include the probability in the label
                info = "{}: {:.2f}%".format(info, max(mask, withoutMask) * 100)
            else:
                i-=1
        elif(i==31 and no>=4 and flag==0):
            ##block
            print("User didn't wore mask - BLOCK")
            label.place(relheight=0.9,relwidth=0.9,relx=0.05,rely=0.05)
            flag=1  ##nomask
            i= -1
            no=0
        elif(i==31 and no<=3 and flag==1):
            ##unblock
            print("User wore mask - UNBLOCK")
            label.place_forget()
            flag=0  ##mask
            i=-1
            no=0
        elif(i==31):
            i=-1
            no=0
        else:
            pass
        # display the label 
        cv2.putText(img, info, (100, 100),cv2.FONT_HERSHEY_SIMPLEX, 1, color, 4)
        i+=1
            
        ##################################################################################
        # 11. Frame Rate
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(wait)
