import socket
import logging

def main():
    logger = logging.getLogger('server_logger')
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler('server_log')

    formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formater)
    logger.addHandler(file_handler)

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('', 45000))
        logger.warning('for connect use parametr socket: socket.AF_INET, socket.SOCK_STREAM')
        logger.warning('for connect use "localhost",  port: 45000')

        sock.listen(10)
        print('server is running')
        logger.info('server is running')
        while True:
            snn, adr = sock.accept()
            print('connected', adr)
            logger.info('connected', adr)
            data = snn.recv(1204)
            print(str(data))
            logger.info(f'data: {str(data)}')
            snn.send(bytes('message from server', encoding = 'UTF-8'))
            logger.warning('use encoding - UTF-8')
        snn.close()
    except Exception as ex:
        print(f'exception error {ex}')
        logger.error(f'exception error {ex}')



if __name__ == '__main__':
    main()

