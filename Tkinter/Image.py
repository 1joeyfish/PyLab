from tkinter import *
from tkinter import ttk
from tkinter import messagebox

image=Tk()

sushilist=[]
desertlist=[]


sushilist.append(PhotoImage(file='sushi.png'))
sushilist.append(PhotoImage(file='sushi2.png'))
sushilist.append(PhotoImage(file='sushi3.png'))
sushilist.append(PhotoImage(file='sushi4.png'))
sushilist.append(PhotoImage(file='sushi5.png'))

desertlist.append(PhotoImage(file='desert.png'))
desertlist.append(PhotoImage(file='desert2.png'))
desertlist.append(PhotoImage(file='desert3.png'))
desertlist.append(PhotoImage(file='desert4.png'))
desertlist.append(PhotoImage(file='desert5.png'))


#insert lableframes

sushiframe=ttk.Labelframe(image,text='Sushi',width='200',height='200')
sushiframe.grid(row=1,column=1,columnspan=3)

desertframe=ttk.Labelframe(image,text='Desert',width='200',height='200')
desertframe.grid(row=1,column=4,columnspan=3)


#display images

sushilabel=ttk.Label(sushiframe,image=sushilist[0])
sushilabel.grid(row=1,column=1)
desertlabel=ttk.Label(desertframe,image=desertlist[0])
desertlabel.grid(row=1,column=1)

x=0
y=0
amountsushi=0
amountdesert=0

#Define commands

def nextsushi():
    global x
    x+=1
    if x>4:
        x=0
    sushilabel.configure(image=sushilist[x])

def nextdesert():
    global y
    y+=1
    if y>4:
        y=0
    desertlabel.configure(image=desertlist[y])

def addsushiFN():
    global amountsushi
    if amountsushi>=10:
        amountsushi=10
        messagebox.showwarning('PLEASE NOTE','Please note that the quantity can not exeed 10!')
    elif amountsushi<10:
        amountsushi+=1
        QuantitySushi.configure(text=amountsushi)

def minussushiFN():
    global amountsushi
    if amountsushi>0:
        amountsushi-=1
        QuantitySushi.configure(text=amountsushi)
    elif amountsushi<=0:
            messagebox.showwarning('PLEASE NOTE','Please note that the quantity can not be below 0!')

def adddesertiFN():
    global amountdesert
    if amountdesert>=10:
        amountdesert=10
        messagebox.showwarning('PLEASE NOTE','Please note that the quantity can not exeed 10!')
    elif amountdesert<10:
        amountdesert+=1
        QuantityDesert.configure(text=amountdesert)

def minusdesertFN():
    global amountdesert
    if amountdesert>0:
        amountdesert-=1
        QuantityDesert.configure(text=amountdesert)
    elif amountdesert<=0:
            messagebox.showwarning('PLEASE NOTE','Please note that the quantity can not be below 0!')

#add buttons

sushinext=ttk.Button(image,text='Next choice...',command=nextsushi)
sushinext.grid(row=2,column=1,columnspan=3)

desertnext=ttk.Button(image,text='Next choice...',command=nextdesert)
desertnext.grid(row=2,column=4,columnspan=3)


addsushi=ttk.Button(image,text='+',command=addsushiFN)
addsushi.grid(row=3,column=1)

minussushi=ttk.Button(image,text='-',command=minussushiFN)
minussushi.grid(row=3,column=3)

adddesert=ttk.Button(image,text='+',command=adddesertiFN)
adddesert.grid(row=3,column=4)

minusdesert=ttk.Button(image,text='-',command=minusdesertFN)
minusdesert.grid(row=3,column=6)

#add lables

QuantitySushi=ttk.Label(image,text='0')
QuantitySushi.grid(row=3,column=2)

QuantityDesert=ttk.Label(image,text='0')
QuantityDesert.grid(row=3,column=5)


#show

image.mainloop()
