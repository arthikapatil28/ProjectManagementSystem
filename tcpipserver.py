import socket
host="localhost"
port=4000
s=socket.socket()
s.bind((host,port))
print("server listening on port:", port)
s.listen(1)
c,addr=s.accept() #returns connection and clinet address
print("connection from :" ,str(addr))
c.send(b"Hello,How are you!")
c.send("bye".encode())
c.close

