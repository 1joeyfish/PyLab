from tkinter import *
from tkinter import ttk
from random import randint
from time import sleep, time

main_interface=Tk()

VALUE=IntVar()
Progress=ttk.Progressbar(main_interface,orient=HORIZONTAL,mode='determinate',maximum=100,variable=VALUE,length=500)
Progress.grid(row=2,column=2)

value=randint(0,100)
VALUE.set(value)


labelValue=StringVar()
percent=Label(main_interface,textvariable=labelValue)
percent.grid(row=3,column=2)

for i in range(0,11):
    VALUE.set(i)
    labelValue.set(str(i))


for i in range(0,10):
    VALUE.set(i)
    labelValue.set(str(i))
    
for i in range(0,10):
    VALUE.set(i)
    labelValue.set(str(i))

    
for i in range(0,10):
    VALUE.set(i)
    labelValue.set(str(i))

main_interface.mainloop()