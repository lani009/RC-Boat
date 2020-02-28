import socket

HOST = 'localhost'
PORT = 1346

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

s.listen(5)
conn, addr = s.accept()
while True:
    print(bin(int.from_bytes(conn.recv(10), byteorder='big', signed=False)))