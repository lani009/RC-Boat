import socket

#define global variables
HOST = "localhost"
PORT = 1346



def main():
    s = serverInit()
    conn, addr = s.accept()

def serverInit():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    return s

if __name__ == "__main__":
    main()




conn, addr = s.accept()
while True:
    print(bin(int.from_bytes(conn.recv(10), byteorder='big', signed=False)))