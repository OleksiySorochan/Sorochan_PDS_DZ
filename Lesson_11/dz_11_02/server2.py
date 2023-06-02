import socket

def convert(data):
    try:
        res = eval(data)
        return str(res)
    except NameError:
        return 'enter numbers'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 45000))
sock.listen(10)
print('Server is working')
while True:
    ann, kvr = sock.accept()
    print('connect', kvr)
    data = ann.recv(1024)
    print(str(data))
    res = 'Vipovid: '+ convert(data)
    print(res)
    ann.send(bytes(res, encoding = 'UTF-8'))
ann.close()