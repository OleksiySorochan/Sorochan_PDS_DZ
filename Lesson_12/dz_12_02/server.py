import socket, asyncio

answer = []
async def addition(a, b):
    await asyncio.sleep(0)
    answer.append(f'addition: {a} + {b} = {a + b}\n')

async def subtraction(a, b):
    await asyncio.sleep(1)
    answer.append(f'subtraction: {a} - {b} = {a - b}\n')

async def multiplication(a, b):
    await asyncio.sleep(2)
    answer.append(f'multiplication: {a} * {b} = {a * b}\n')

def tasks(data):
    a, b = data.split(' ')
    a = int(a)
    b = int(b)
    io = asyncio.get_event_loop()
    tas = [
        io.create_task(addition(a, b)),
        io.create_task(multiplication(a, b)),
        io.create_task(subtraction(a, b))
    ]
    wait_tas = asyncio.wait(tas)
    io.run_until_complete(wait_tas)
    io.close()




if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 45000))
    sock.listen(10)
    print('server is working')
    while True:
        con, adr = sock.accept()
        print('connected', adr)
        data = con.recv(1024)
        print(data)
        tasks(data.decode('UTF-8'))
        answer = ' '.join(answer)
        print(answer)
        con.send(bytes(answer, encoding = 'UTF-8'))
    con.close()




