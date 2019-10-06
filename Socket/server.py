import socket

ipinfo=('192.168.1.18',50000) # Server Address
#ipinfo=('127.0.0.1',50000)

socketobj = socket.socket() # Create socket object#
socketobj.bind(ipinfo)      # bind server address
socketobj.listen(5)         # Listening client
conn,client_address = socketobj.accept()  # Accept connection from client
print('client address =',client_address) 
print('Maximun characters is 1024.')

while True:
    message = input('>>> ')     #Ask for the message
    conn.send(message.encode())     # encode message and send to client
    recivemess = conn.recv(1024).decode() # Receive message from client
    print(str(recivemess))
conn.close()    # close connection
socketobj.close()   # close socket object.