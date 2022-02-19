from tkinter import *
from basic import frame,clear_frame,bgcolor
from page3_1 import page3_1

def page2():
    clear_frame()
    labelfont = ('Helvetica', 50, 'bold')
    ins1=Label(frame,text='Please insert your Card in the card reader',bg=bgcolor,fg="white",height=3)
    ins1.config(font = labelfont)
    ins1.pack(fill=X,pady=100)

    labelfont = ('Helvetica', 25, 'bold')
    next_btn = Button(frame,text="Next",bg="#e6a919",command=page3_1,height=3)
    next_btn.config(font = labelfont)
    next_btn.pack(anchor="center",ipadx=200)
