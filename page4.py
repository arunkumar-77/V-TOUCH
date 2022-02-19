from tkinter import *
from basic import frame,clear_frame,bgcolor
from page7 import page7
from page5 import page5


def page4():
    clear_frame()

    labelfont = ('Helvetica', 40, 'bold')
    ins1=Label(frame,text='Enter the Amount',bg=bgcolor,fg="white",font=labelfont)
    ins1.place(relx=0.35,rely=0.03)

    frame2 = Frame(frame, bg=bgcolor)
    frame2.place(relheight=0.85, relwidth=0.9,relx=0.05,rely=0.1)

    amount = StringVar()  #since the value updates continously we use textvariable
    labelfont = ('Helvetica', 15, 'bold')
    l = Label(frame2,textvariable=amount,borderwidth=5,width=110)
    l.grid(row=0,column=0,columnspan=4,padx=10,pady=20,ipady=40)

    def number(x):
        total=amount.get()+x
        amount.set(total)

    def delete():
        amount.set(amount.get()[:-1])

    def clear():
        amount.set("")

    w = 27
    labelfont = ('Helvetica', 15, 'bold')

    def cancel():
        print("Transaction Cancelled")
        page7()
    
    def next():
        print("Entered Amount : ",amount.get())
        page5()

    button_7=Button(frame2,text=" 7",width=w,pady=20,height=3,command=lambda: number("7"),font=labelfont)
    button_8=Button(frame2,text="8",width=w,pady=20,height=3,command=lambda: number("8"),font=labelfont)
    button_9=Button(frame2,text="9",width=w,pady=20,height=3,command=lambda: number("9"),font=labelfont)
    button_x=Button(frame2,text="x",width=w,pady=20,height=3,command=delete,font=labelfont)
    
    button_4=Button(frame2,text=" 4",width=w,pady=20,height=3,command=lambda: number("4"),font=labelfont)
    button_5=Button(frame2,text="5",width=w,pady=20,height=3,command=lambda: number("5"),font=labelfont)
    button_6=Button(frame2,text="6",width=w,pady=20,height=3,command=lambda: number("6"),font=labelfont)
    button_clear=Button(frame2,text="Clear",width=w,height=3,pady=20,command=clear,font=labelfont)

    button_1=Button(frame2,text=" 1",width=w,pady=20,height=3,command=lambda: number("1"),font=labelfont)
    button_2=Button(frame2,text="2",width=w,pady=20,height=3,command=lambda: number("2"),font=labelfont)
    button_3=Button(frame2,text="3",width=w,pady=20,height=3,command=lambda: number("3"),font=labelfont)
    button_cancel=Button(frame2,text="Cancel",width=w,pady=20,height=3,command=cancel,font=labelfont)

    button_00=Button(frame2,text="00",width=w,pady=20,height=3,command=lambda: number("00"),font=labelfont)
    button_0=Button(frame2,text="0",width=2*w+1,pady=20,height=3,command=lambda: number("0"),font=labelfont)
    button_next=Button(frame2,text="Next",width=w,height=3,pady=20,command=next,font=labelfont)

    button_7.grid(row=1,column=0,padx=10,pady=10)
    button_8.grid(row=1,column=1,padx=10,pady=10)
    button_9.grid(row=1,column=2,padx=10,pady=10)
    button_x.grid(row=1,column=3,padx=10,pady=10)

    button_4.grid(row=2,column=0,padx=10,pady=10)
    button_5.grid(row=2,column=1,padx=10,pady=10)
    button_6.grid(row=2,column=2,padx=10,pady=10)
    button_clear.grid(row=2,column=3,padx=10,pady=10)

    button_1.grid(row=3,column=0,padx=10,pady=10)
    button_2.grid(row=3,column=1,padx=10,pady=10)
    button_3.grid(row=3,column=2,padx=10,pady=10)
    button_cancel.grid(row=3,column=3,padx=10,pady=10)

    button_00.grid(row=4,column=0,padx=10,pady=10)
    button_0.grid(row=4,columnspan=2,column=1,padx=10,pady=10)
    button_next.grid(row=4,column=3,padx=10,pady=10)