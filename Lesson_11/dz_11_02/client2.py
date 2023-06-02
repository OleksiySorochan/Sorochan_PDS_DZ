import socket

while True:
    data = input('Введтіь числа для обчислення: ')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 45000))
    sock.send(bytes(data, encoding='UTF-8'))
    answer = sock.recv(1024)
    sock.close()
    print(str(answer))
    if data == 'stop':
        break

