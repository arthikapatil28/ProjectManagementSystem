import socket
s=socket.socket()
s.connect(("localhost",4000))
filename=input("Enter the file name: ")
s.send(filename.encode())
content=s.recv(1024)
print(content.decode())
s.close()