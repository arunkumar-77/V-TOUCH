from tkinter import *
from basic import frame,clear_frame,bgcolor
from page6 import page6
from threading import Timer

def page5():
    clear_frame()

    labelfont = ('Helvetica', 50, 'bold')
    ins1=Label(frame,text='Please wait while processing..',bg=bgcolor,fg="white",height=3)
    ins1.config(font = labelfont)
    ins1.pack(pady=300)
    r = Timer(2.0, page6)
    r.start()