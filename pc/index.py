import keyboard as key
import time

def main():
    key.on_release_key("`", zeroSpeed)
    key.on_press_key("1", gearOne)
    key.on_press_key("2", gearTwo)
    key.on_press_key("3", gearThree)
    key.on_press_key("4", fullSpeed)
    while True:
        time.sleep(0.05)
        if key.is_pressed("left"):
            turnLeft()
        if key.is_pressed("right"):
            turnRight()
        if key.is_pressed("w"):
            throttleUp()
        if key.is_pressed("s"):
            throttleDown()
        # if key.is_pressed("0"):
        #     zeroSpeed()
        # if key.is_pressed("1"):
        #     gearOne()
        # if key.is_pressed("2"):
        #     gearTwo()
        # if key.is_pressed("3"):
        #     gearThree()
        # if key.is_pressed("4"):
        #     fullSpeed()
    

#0, 25%, 50%, 75%, 100%
def zeroSpeed(a):
    pass

def gearOne():
    pass

def gearTwo():
    pass

def gearThree():
    pass

def fullSpeed():
    pass



def turnLeft():
    pass

def turnRight():
    pass

def throttleUp():
    pass

def throttleDown():
    pass

def call(a):
    print(a)
if __name__ == "__main__":
    main()