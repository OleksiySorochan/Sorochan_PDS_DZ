import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 45000))
sock.listen(10)
print('server is running')
while True:
    snn, adr = sock.accept()
    print('connected', adr)
    data = snn.recv(1204)
    print(str(data))
    snn.send(bytes('message from server', encoding = 'UTF-8'))
snn.close()