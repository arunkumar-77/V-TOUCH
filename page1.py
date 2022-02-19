from tkinter import *
from basic import frame,clear_frame,bgcolor,engine
from page2 import page2

def page1():

    clear_frame()
    labelfont = ('Helvetica', 120, 'bold')
    head=Label(frame,text='V-TOUCH',bg=bgcolor,fg="white",height=2)
    head.config(font = labelfont)
    head.pack(fill=X)

    labelfont = ('Helvetica', 50, 'bold')
    ins1 = Label(frame,text="Welcome to V-TOUCH",bg=bgcolor,fg="white")
    ins1.config(font = labelfont)
    ins1.pack(fill=X,pady=20)

    labelfont = ('Helvetica', 25, 'bold')
    ins2 = Label(frame,text="Please wear your MASK",bg=bgcolor,fg="white")
    ins2.config(font = labelfont)
    ins2.pack(fill=X,pady=10)

    ins3 = Label(frame,text="And raise your palm to get control of POINTER",bg=bgcolor,fg="white")
    ins3.config(font = labelfont)
    ins3.pack(fill=X)

    text = "Welcome to V touch. Please wear your mask and raise your palm to get control of pointer"
    engine.say(text)
    engine.runAndWait()

    labelfont = ('Helvetica', 25, 'bold')
    next_btn = Button(frame,text="Next",bg="#e6a919",command=page2)
    next_btn.config(font = labelfont)
    next_btn.pack(anchor="center",pady=50,ipadx=80,ipady=50)
