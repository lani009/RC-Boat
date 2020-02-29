import socket

HOST = ''
PORT = 1346

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

s.listen(1)
conn, addr = s.accept()
try:
    while True:
        raw_data = conn.recv(10)
        if not raw_data:
            raise Exception("client server closed")
        data = int.from_bytes(raw_data, byteorder='big', signed=False)
        speed = data >> 2
        direction = data & 3
        if direction == 0:
            temp = '좌'
        elif direction == 1:
            temp = '우'
        elif direction == 2:
            temp = '중'

        print(speed, temp)
        conn.sendall(raw_data)
except Exception as e:
    print(e)
finally:
    print("out")
    conn.close()
    s.close()