from tkinter import *
from basic import frame,clear_frame,bgcolor,engine

def page7():
    clear_frame()

    print("Transaction Successful")

    labelfont = ('Helvetica', 100, 'bold')
    ins1=Label(frame,text='WELCOME',bg=bgcolor,fg="white")
    ins1.config(font = labelfont)
    ins1.place(relx=0.25,rely=0.3)

    labelfont = ('Helvetica', 60, 'bold')
    ins2=Label(frame,text='Thanks for using V-TOUCH',bg=bgcolor,fg="white")
    ins2.config(font = labelfont)
    ins2.place(relx=0.15,rely=0.5)

    text = "Thanks for using V-TOUCH"
    engine.say(text)
    engine.runAndWait()
    
