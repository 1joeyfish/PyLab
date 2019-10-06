import socket

#ipinfo=('192.168.1.18',50000)
ipinfo=('127.0.0.1',50000)
#Create socket object#
socketobj = socket.socket()
socketobj.connect(ipinfo)

while True:
    recivemess = socketobj.recv(1024).decode()
    print(str(recivemess))
    message = input('>>> ')
    socketobj.send(message.encode())
socketobj.close()