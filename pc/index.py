import keyboard as key
import time

speedKey = []
def main():
    speedKey.append(key.on_press_key("`", zeroSpeed))
    speedKey.append(key.on_press_key("1", gearOne))
    speedKey.append(key.on_press_key("2", gearTwo))
    speedKey.append(key.on_press_key("3", gearThree))
    speedKey.append(key.on_press_key("4", fullSpeed))

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
def zeroSpeed(e):
    print(e)

def gearOne(e):
    print(e)

def gearTwo(e):
    pass

def gearThree(e):
    pass

def fullSpeed(e):
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