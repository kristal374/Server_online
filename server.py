import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('192.168.1.6', 53210))
c.sendall(b'Hello, world')
data = c.recv(1024)
c.close()
print('Received', repr(data))
