import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('localhost', 53210))
print('local host')
c.sendall(b'Hello, world')
data = c.recv(1024)
c.close()
print('Received', repr(data))
