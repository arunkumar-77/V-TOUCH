from tkinter import *
from basic import frame,clear_frame,bgcolor
from page3_2 import page3_2
from page7 import page7
from threading import Timer

def page3_1():

        clear_frame()
        labelfont = ('Helvetica',60, 'bold')
        ins1=Label(frame,text='Enter the PIN',bg=bgcolor,fg="white")
        ins1.config(font = labelfont)
        ins1.place(relx=0.33,rely=0.1)

        pinholder = Label(frame,text="",fg="black")
        pinholder.place(relx=0.3,rely=0.3,relheight=0.15,relwidth=0.4)

        labelfont = ('Helvetica', 25, 'bold')
        cancel = Button(frame,text="Cancel",bg="#e6a919",state=DISABLED,command=lambda:page7)
        cancel.config(font = labelfont)
        cancel.place(relx=0.05,rely=0.55,relheight=0.2,relwidth=0.25)

        labelfont = ('Helvetica', 25, 'bold')
        re_btn = Button(frame,text="Re-enter",bg="#e6a919",state=DISABLED)
        re_btn.config(font = labelfont)
        re_btn.place(relx=0.37,rely=0.55,relheight=0.2,relwidth=0.25)

        labelfont = ('Helvetica', 25, 'bold')
        next_btn = Button(frame,text="Next",bg="#e6a919",state=DISABLED)
        next_btn.config(font = labelfont)
        next_btn.place(relx=0.7,rely=0.55,relheight=0.2,relwidth=0.25)

        labelfont = ('Helvetica', 20, 'bold')
        note = Label(frame,text="Enter your PIN with zero seperated\nEg : If your PIN is 12345 then enter 0102030405",bg=bgcolor,fg="white")
        note.config(font = labelfont)
        note.place(relx=0.3,rely=0.85)

        r = Timer(1.0, page3_2)
        r.start()