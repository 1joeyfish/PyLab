from tkinter import *
from tkinter import ttk

sushiGUI=Tk()
sushiGUI.title('Place order')

Menuframe=ttk.LabelFrame(sushiGUI,text='Menu')
Menuframe.grid(row=1,column=1)

mylist=['Appetizer','Entree','Pizza','Sashimi','Soup','Desert']
mylist2=StringVar(value=mylist)


foodlist=Listbox(Menuframe,listvariable=mylist2)
foodlist.grid(row=1,column=1)









sushiGUI.mainloop()