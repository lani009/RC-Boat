from socket import *

socket = socket(AF_INET, SOCK_STREAM)
socket.bind(('', 1346))
socket.listen()


def main():
    pass


if __name__ == "__main__":
    main()