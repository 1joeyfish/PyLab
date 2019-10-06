from tkinter import *
from tkinter import ttk
import socket
from threading import Thread

def accpet():
    conn,client_address = socketobj.accept()  # Accept connection from client
    connect['Conn']=conn
    text.insert(END,'%s:%s has connected.'%client_address+'\n')
    connect['Conn'].send('You have connected.'.encode())

    while True:
        recivemess = conn.recv(1024).decode() # Receive message from client
        text.insert(END,'Client: '+recivemess+'\n\n')

def send(event=None):
    if mesent.get()=='q!':
        connect['Conn'].close()
        text.insert(END,'Connection closed. Try later.')
    else:
        text.insert(END,'Server: '+mesent.get()+'\n\n')
        connect['Conn'].send(mesent.get().encode())     # encode message and send to client
        mesent.delete(first=0,last=END)
#-------------------------------------------------------------------
#Create GUI


server=Tk()
server.title('Server')

text=Text(server)
text.grid(row=1,column=1,rowspan=4,columnspan=9)
text.insert(END,'Processing...\n\n')
#text.config(state=DISABLED)

mesent=ttk.Entry(server,width=105)
mesent.bind("<Return>",send)
mesent.grid(row=5,column=1,rowspan=2,columnspan=8)

send=ttk.Button(server,text='>',command=send)
send.grid(row=5,column=9,rowspan=2)
#-------------------------------------------------------------------
#Socket preformance

connect={}

ipinfo=('192.168.1.18',50000) # Server Address
#ipinfo=('127.0.0.1',50000)

socketobj = socket.socket() # Create socket object#
socketobj.bind(ipinfo)      # bind server address
socketobj.listen(5)         # Listening client

st=Thread(target=accpet)
st.start()

server.mainloop()
socketobj.close()   # close socket object.