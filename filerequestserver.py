import socket
socket.socket()
s.bind(("localhost",4000))
s.listen(1)
c,addr=s.accept()
fileName=c.recv(1024)
try:
    f=open(fileName,"rb")
    content=f.read()
    c.send(content)
    f.close()
except FileNotFoundError:
    c.send(b"file Does Not exist")
c.close()
    