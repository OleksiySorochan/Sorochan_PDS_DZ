import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 45000))
sock.send(bytes('message from client', encoding = 'UTF-8'))
data = sock.recv(1024)
sock.close()
print(str(data))