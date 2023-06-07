import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 45000))
data = input('Введіть два числа через пробіл: ')
sock.send(bytes(data, encoding = 'UTF-8'))
answer = sock.recv(1024)
sock.close()
print(answer.decode('UTF-8'))
