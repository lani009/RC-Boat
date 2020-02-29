import socket

HOST = 'localhost'
PORT = 1346

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

s.listen(1)
conn, addr = s.accept()
while True:
    data = int.from_bytes(conn.recv(10), byteorder='big', signed=False)
    speed = data >> 2
    direction = data & 3
    if direction == 0:
        temp = '좌'
    elif direction == 1:
        temp = '우'
    elif direction == 2:
        temp = '중'

    print(speed, temp)