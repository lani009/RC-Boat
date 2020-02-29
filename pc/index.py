import keyboard as key
import time
import socket

#global variables
PORT = 1346
#state = [speed, direction]
state = [0, 0]


def main():
    #socket Instance
    s = connect()

    left = False
    right = False
    while True:
        #10Hz Comm
        time.sleep(0.1)
        data = 0
        state[1] = 2
        if key.is_pressed("`"):
            zeroSpeed()
        if key.is_pressed("1"):
            gearOne()
        if key.is_pressed("2"):
            gearTwo()
        if key.is_pressed("3"):
            gearThree()
        if key.is_pressed("4"):
            fullSpeed()
        left = key.is_pressed("left")
        right = key.is_pressed("right")
        #if the left button and right button pushed
        #simultaneously, prints nutural direction
        if left and right:
            state[1] = 2
        else:
            if left:
                turnLeft()
            if right:
                turnRight()
        if key.is_pressed("w"):
            throttleUp()
        if key.is_pressed("s"):
            throttleDown()
        if key.is_pressed("ctrl+q"):
            off(s)

        data |= state[0] << 2
        data |= state[1]
        byte = bytearray()
        byte.append(data)
        s.send(byte)
    

def connect():
    print("***** RC-Boat *****\nInitialize")
    IP = input("ip Address: ")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP, PORT))
        print("socket connection success!")
    except:
        print("server error")
        exit()
    return s

#0, 25%, 50%, 75%, 100%
def zeroSpeed():
    state[0] = 0

def gearOne():
    state[0] = 1    #00100

def gearTwo():
    state[0] = 2    #01000

def gearThree():
    state[0] = 3    #01100

def fullSpeed():
    state[0] = 4    #10000

def turnLeft():
    state[1] = 0

def turnRight():
    state[1] = 1

def throttleUp():
    if(state[0] > 3):
        pass
    else:
        state[0] += 1

def throttleDown():
    if(state[0] < 1):
        pass
    else:
        state[0] -= 1

def off(s):
    s.close()
    exit()


if __name__ == "__main__":
    main()