from socket import *

while True:
    clientSock = socket(AF_INET, SOCK_STREAM)
    clientSock.connect(('192.168.0.10', 8080))

    print('연결 확인 됐습니다.')
    way = input()
    clientSock.send(way.encode('utf-8'))

    print('신호를 전송했습니다.')

    data = clientSock.recv(1024)
    # print('받은 데이터 : ', data.decode('utf-8'))
    if way == 'quit':
        break

