from tkinter import *
from basic import frame,clear_frame,bgcolor
from page7 import page7
from threading import Timer

def page6():
    clear_frame()

    labelfont = ('Helvetica', 60, 'bold')
    ins1=Label(frame,text='Remove your Card',bg=bgcolor,fg="white")
    ins1.config(font = labelfont)
    ins1.place(relx=0.3,rely=0.3)

    ins2=Label(frame,text='And Collect your cash',bg=bgcolor,fg="white")
    ins2.config(font = labelfont)
    ins2.place(relx=0.25,rely=0.5)
    
    r = Timer(2.0, page7)
    r.start()