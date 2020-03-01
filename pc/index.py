import os
import socket
import time

import keyboard as key

#global variables
PORT = 1346
#state = [speed, direction]
state = [0, 0]
#Continuous Input Protection
continuous = False

def main():
    global continuous

    #socket Instance
    s = connect()

    left = False
    right = False
    while True:
        #10Hz Comm
        time.sleep(0.1)
        data = 0
        state[1] = 2
        if key.is_pressed("z"):
            zeroSpeed()
        if key.is_pressed("x"):
            gearOne()
        if key.is_pressed("c"):
            gearTwo()
        if key.is_pressed("v"):
            gearThree()
        if key.is_pressed("space"):
            fullSpeed()
        if key.is_pressed("b"):
            reverseSpeed()
        left = key.is_pressed("left")
        right = key.is_pressed("right")
        #if left button and right button pushed
        #simultaneously, prints nutural direction
        if left and right:
            state[1] = 2
        else:
            if left:
                turnLeft()
            if right:
                turnRight()
        if continuous and not (key.is_pressed("w") or key.is_pressed("s")):
            continuous = False
        if not continuous and key.is_pressed("w"):
            throttleUp()
        if not continuous and key.is_pressed("s"):
            throttleDown()
        if key.is_pressed("ctrl+q"):
            s.close()
            print("connection closed")
            break
        data |= state[0] << 2
        data |= state[1]
        byte = bytearray()
        byte.append(data)
        #state data sending via socket connection
        s.send(byte)
        printBoatStatus(s.recv(4))

def connect():
    '''socket server connect'''
    print("***** RC-Boat *****\nInitialize")
    IP = input("ip Address: ")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP, PORT))
        print("socket connection success!")
    except Exception as e:
        print("server error", e)
    #returns the socket instance
    return s

def printBoatStatus(raw_data):
    os.system("cls")
    data = int.from_bytes(raw_data, byteorder='big', signed=False)

    print("voltage: {}".format(data))

def zeroSpeed():
    state[0] = 0    #00000

def gearOne():
    state[0] = 1    #00100

def gearTwo():
    state[0] = 2    #01000

def gearThree():
    state[0] = 3    #01100

def fullSpeed():
    state[0] = 4    #10000

def reverseSpeed():
    state[0] = 5

def turnLeft():
    state[1] = 0    #00000

def turnRight():
    state[1] = 1    #00001

def throttleUp():
    global continuous
    if(state[0] > 3):
        pass
    else:
        state[0] += 1
    continuous = True

def throttleDown():
    global continuous
    if(state[0] < 1):
        pass
    else:
        state[0] -= 1
    continuous = True

if __name__ == "__main__":
    main()
