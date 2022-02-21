###################packages necessary for page3_2############################

from tkinter import *
from tkinter import messagebox
from basic import frame,clear_frame,bgcolor
from page4 import page4

###################packages necessary for finger_counter######################

import cv2
import time
import mediapipe as mp
from page7 import page7

#list for holding pins
pin = [-1]
#############################updating PIN column#############################

next=0
prev=""
ans = ""
close=0
def updated(x):
    global pinholder,prev    
    ans = prev + str(x)
    encoded=ans
    for i in range(1,6):
        encoded = encoded.replace(str(i),"*")
    pinholder = Label(frame, text=encoded, fg="black")
    pinholder.place(relx=0.3, rely=0.3, relheight=0.15, relwidth=0.4)
    prev = ans

def re_enter(x):
    print("Re-entering PIN")
    if x==1:
        messagebox.showwarning("warning","Enter zero seperated PIN with zero at beginning")
    global pin
    pin=[-1]
    global ans,prev
    ans=""
    prev=""
    pinholder = Label(frame, text=ans, fg="black")
    pinholder.place(relx=0.3, rely=0.3, relheight=0.15, relwidth=0.4)

########################### finger_counter function ###########################

def finger_counter():

    # Displaying Number
    def getNumber(ar):
        s = ""
        for i in ar:
            s += str(i);
        if (s == "00000"):
            return (0)
        elif (s == "01000" or s == "00010"):
            return (1)
        elif (s == "01100" or s == "00110"):
            return (2)
        elif (s == "00111" or s == "11100"):
            return (3)
        elif (s == "01111" or s == "11110"):
            return (4)
        elif (s == "11111"):
            return (5)
        else:
            return(-1)

    # Setting Webcam Parameters
    wcam, hcam = 640, 480
    global cap
    cap = cv2.VideoCapture(1)
    cap.set(3, wcam+200)
    cap.set(4, hcam+200)
    pTime = 0  # Previous Time

    mpHands = mp.solutions.hands
    #hands = mpHands.Hands(False,2,0.5,0.5)
    hands = mpHands.Hands()
    mpDraw = mp.solutions.drawing_utils

    #Dictionary for numbers
    num = {
        0 : 0,
        1 : 0,
        2 : 0,
        3 : 0,
        4 : 0,
        5 : 0
    }

    # When the Webcam turned on
    while True:   
        success, img = cap.read()
        # Calling handDetector Methods
        #img = detector.findHands(img, draw=True)
    ################################################################
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # completes the image processing.
        results = hands.process(imgRGB)
            # print(self.results)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                if True:
                    # mpDraw.draw_landmarks - drawing land marks of hands and
                    # mpHands.HAND_CONNECTIONS - hand connection
                    mpDraw.draw_landmarks(img, handLms,
                                                mpHands.HAND_CONNECTIONS)
    ############################################################################
        #lmList = detector.findPosition(img, draw=False)
        lmList = []
        if results.multi_hand_landmarks:
            myHand = results.multi_hand_landmarks[0]
            for id, lm in enumerate(myHand.landmark):
                # h - height, w - weight, c - channels
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                lmList.append([id, cx, cy])
                if False:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
    ##############################################################################################
            
        # tip Id or each finger - thumb, index, middle finger, ring finger, and little finger or pinkie
        tipId = [4, 8, 12, 16, 20]

        # If the list is not empty (i.e it finally finds position of hand)
        if (len(lmList) != 0):
            fingers = []
            ## finding left or right hand and changing thumb coordinates
            if(lmList[tipId[0]][1] <= lmList[tipId[4]][1]):
                # thumb - thumb_TIP > thumb_IP
                if (lmList[tipId[0]][1] >= lmList[tipId[0] - 1][1] ):
                    fingers.append(0)
                else:
                    fingers.append(1)
            else:
                if (lmList[tipId[0]][1] <= lmList[tipId[0] - 1][1] ):
                    fingers.append(0)
                else:
                    fingers.append(1)

            # 4 fingers - TIP < DIP
            for id in range(1, len(tipId)):

                if (lmList[tipId[id]][2] < lmList[tipId[id] - 2][2]):
                    fingers.append(1)

                else:
                    fingers.append(0)


            # Putting rectangle box around numbers
            # SYNTAX - cv2.rectangle(image, start_point, end_point, color, thickness)
            cv2.rectangle(img, (20, 255), (170, 425), (0, 255, 0), cv2.FILLED)
            val = getNumber(fingers)
            
            if val==-1: #for unknown finger formats
                pass
            
            else :
                cv2.putText(img, str(val), (45, 375), cv2.FONT_HERSHEY_PLAIN,
                            10, (255, 0, 0), 20)

                num[val]+=1

                reinit = 0
                for k,v in num.items():
                    global pin
                    if v>=15 and pin[-1]!=k:
                        if (len(pin)-1)%2==0 and k!=0:
                            re_enter(1)                            
                        else :
                            pin.append(k)
                            #reinitializing the num
                            updated(k)
                        reinit = 1
                        break
                
                if reinit==1 :
                    num.update({0 : 0, 1 : 0, 2 : 0, 3 : 0, 4:0 , 5:0})


        cTime = time.time()  # Current Time
        # Calculating the fps
        # fps will be number of frame processed in given time frame
        # since their will be most of time error of 0.001 second
        # we will be subtracting it to get more accurate result
        fps = 1 / (cTime - pTime)

        # Then we will change the previous time from 0 to current time
        pTime = cTime

        # SYNTAX - cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]
        cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 3)

        # Showing Image
        cv2.imshow("image", img)

        if (cv2.waitKey(2) & 0xFF == ord('q')) or (len(pin)==11) or close==1:
            break
    

    #cap.release()
    #cv2.destroyAllWindows()
    pin = [str(i) for i in pin if i]
    pin= pin[1:]
    if(close==0):
        print("PIN : ","".join(pin))
    return



def fn():
    global close
    close=1
    print("Transaction Cancelled")
    page7()


############################### page3_2 function ##############################
def page3_2():

    labelfont = ('Helvetica', 25, 'bold')
    cancel = Button(frame,text="Cancel",bg="#e6a919",command=fn)
    cancel.config(font = labelfont)
    cancel.place(relx=0.05,rely=0.55,relheight=0.2,relwidth=0.25)
            
    re_btn = Button(frame,text="Re-enter",bg="#e6a919",command=lambda:re_enter(0))
    re_btn.config(font = labelfont)
    re_btn.place(relx=0.37,rely=0.55,relheight=0.2,relwidth=0.25)

    finger_counter()

    #print(ans)
    #pinholder = Label(frame, textvariable=ans, fg="black")
    #pinholder.place(relx=0.3, rely=0.3, relheight=0.15, relwidth=0.4)

    if close==0:

        re_btn = Button(frame,text="Re-enter",bg="#e6a919",command=lambda:re_enter(0),state=DISABLED)
        re_btn.config(font = labelfont)
        re_btn.place(relx=0.37,rely=0.55,relheight=0.2,relwidth=0.25)

        labelfont = ('Helvetica', 25, 'bold')
        next_btn = Button(frame,text="Next",bg="#e6a919",command=page4)
        next_btn.config(font = labelfont)
        next_btn.place(relx=0.7,rely=0.55,relheight=0.2,relwidth=0.25)
