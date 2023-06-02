import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 51000))
sock.listen(10)
print('server is working')
while True:
    con, adr = sock.accept()
    print('connected: ', adr)
    data = con.recv(1024)
    print(str(data))
    ld = str(data).split(' ')
    answer = f'Answer: {str(len(ld))}'
    print(answer)
    con.send(bytes(answer, encoding = 'UTF-8'))
con.close()