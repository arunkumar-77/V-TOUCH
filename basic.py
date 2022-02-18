from tkinter import *
import autopy
import pyttsx3

###########################################################
engine = pyttsx3.init()

# """VOLUME"""
#volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
#print (volume)                          #printing current volume level
engine.setProperty('volume',1)

# """VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id)  

# """Rate"""
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

############################################################

xlen, ylen = autopy.screen.size()
bgcolor = "#053365"

root = Tk()
root.title("V-TOUCH")
dim = str(int(xlen*1.2))+"x"+str(int(ylen*1.3))
# dim="1600x800"
root.geometry(dim)
frame = Frame(root,bg=bgcolor)
frame.place(relheight=1.0,relwidth=1.0)

def clear_frame():
    for widgets in frame.winfo_children():
        widgets.destroy()