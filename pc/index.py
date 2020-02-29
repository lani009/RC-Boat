import keyboard as key
import time
import socket

#global variables
PORT = 1346
#state = [speed, direction]
state = [0, 0]
#Continuous Input Protection
continuous = False

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
        if key.is_pressed("w") and not continuous:
            throttleUp()
        if key.is_pressed("s") and not continuous:
            throttleDown()
        if key.is_pressed("ctrl+q"):
            s.close()
            break
        data |= state[0] << 2
        data |= state[1]
        byte = bytearray()
        byte.append(data)
        #state data sending via socket connection
        s.send(byte)

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

def turnLeft():
    state[1] = 0    #00000

def turnRight():
    state[1] = 1    #00001

def throttleUp():
    if(state[0] > 3):
        pass
    else:
        state[0] += 1
    continuous = True

def throttleDown():
    if(state[0] < 1):
        pass
    else:
        state[0] -= 1
    continuous = True

def off(s):
    s.close()
    exit()

if __name__ == "__main__":
    main()