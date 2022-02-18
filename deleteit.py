from basic import frame
from tkinter import *
from tkinter import messagebox
import time

def hide_widget(widget):
   widget.pack_forget()

#Define a function to show the widget
def show_widget(widget):
   widget.pack()


def fn():
    label= Label(frame, text= "Showing the Message", font= ('Helvetica bold', 14))
    label.pack(pady=20)
    time.sleep(10)
    # hide_widget(label)
    label.config(state=DISABLED)
    time.sleep(10)
    # show_widget(label)
    label.config(state=ACTIVE)





