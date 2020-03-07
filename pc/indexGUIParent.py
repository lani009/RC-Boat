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
class indexGUIParent:

    def __init__(self, PORT, IP):
        self.Port = PORT
        self.IP = IP

    def main(self):
        global continuous

        #socket Instance
        s = self.connect()

        left = False
        right = False
        while True:
            #10Hz Comm
            time.sleep(0.1)
            data = 0
            state[1] = 2
            if key.is_pressed("z"):
                self.zeroSpeed()
            if key.is_pressed("x"):
                self.gearOne()
            if key.is_pressed("c"):
                self.gearTwo()
            if key.is_pressed("v"):
                self.gearThree()
            if key.is_pressed("space"):
                self.fullSpeed()
            if key.is_pressed("b"):
                self.reverseSpeed()
            left = key.is_pressed("left")
            right = key.is_pressed("right")
            #if left button and right button pushed
            #simultaneously, prints nutural direction
            if left and right:
                state[1] = 2
            else:
                if left:
                    self.turnLeft()
                if right:
                    self.turnRight()
            if continuous and not (key.is_pressed("w") or key.is_pressed("s")):
                continuous = False
            if not continuous and key.is_pressed("w"):
                self.throttleUp()
            if not continuous and key.is_pressed("s"):
                self.throttleDown()
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
            self.printBoatStatus(s.recv(4))

    def connect(self):
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

    def printBoatStatus(self, raw_data):
        os.system("cls")
        data = int.from_bytes(raw_data, byteorder='big', signed=False)

        print("voltage: {}".format(data))

    def zeroSpeed(self):
        state[0] = 0    #00000

    def gearOne(self):
        state[0] = 1    #00100

    def gearTwo(self):
        state[0] = 2    #01000

    def gearThree(self):
        state[0] = 3    #01100

    def fullSpeed(self):
        state[0] = 4    #10000

    def reverseSpeed(self):
        state[0] = 5

    def turnLeft(self):
        state[1] = 0    #00000

    def turnRight(self):
        state[1] = 1    #00001

    def throttleUp(self):
        global continuous
        if(state[0] > 3):
            pass
        else:
            state[0] += 1
        continuous = True

    def throttleDown(self):
        global continuous
        if(state[0] < 1):
            pass
        else:
            state[0] -= 1
        continuous = True

if __name__ == "__main__":
    a=indexGUIParent(PORT, None)
    a.main()