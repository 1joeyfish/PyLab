from tkinter import *
from tkinter import ttk
import socket
from threading import Thread

def send(event=None):
    if mesent.get()=='q!':
        socketobj.close()
        text.insert(END,'Connection closed. Try later.')
    else:
        text.insert(END,'Client: '+mesent.get()+'\n\n')
        socketobj.send(mesent.get().encode())
        mesent.delete(first=0,last=END)

def recive():
    while True:
        recivemess = socketobj.recv(1024).decode()
        text.insert(END,'Server: '+recivemess+'\n\n')
#-------------------------------------------------------------------
#Create GUI
client=Tk()
client.title('Client')

text=Text(client)
text.grid(row=1,column=1,rowspan=3,columnspan=7)
text.insert(END,'Processing...\n\n')
#text.config(state=DISABLED)

mesent=ttk.Entry(client,width=105)
mesent.bind("<Return>",send)
mesent.grid(row=4,column=1,columnspan=6)

send=ttk.Button(client,text='>',command=send)
send.grid(row=4,column=8)
#-------------------------------------------------------------------
#Socket preformance

#ipinfo=('192.168.1.18',50000)
ipinfo=('127.0.0.1',50000)
#Create socket object#
socketobj = socket.socket()
socketobj.connect(ipinfo)

st=Thread(target=recive)
st.start()

client.mainloop()
socketobj.close()