import socket
import time
import RPi.GPIO as GPIO

#define global variables -> constant
HOST_ = "localhost"
PORT_ = 1346

#GPIO Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)

servo = GPIO.PWM(11,50)
bright = GPIO.PWM(7,100)
servo.start(0)

class ANGLE():
    '''ANGLE CONSTANT'''
    LEFT = 9.35     #-29.7 degree
    RIGHT = 5.65    #0 degree
    NEUTRAL = 7.5   #29.7 degree

def main():
    try:
        s = serverInit()
        conn, addr = s.accept()
        print("Connection accepted")
        while True:
            speed, direction = parseData(int.from_bytes(conn.recv(10), byteorder='big', signed=False))
            changeRudderAngle(direction)
            changeSpeed(speed)
    except:
        pass
    finally:
        s.close()
        GPIO.cleanup()
        print("Connection Closed!")
        

def parseData(data):
    speed = data >> 2
    direction = data & 3
    return (speed, direction)

def changeRudderAngle(direction):
    if direction == 0:
        servo.ChangeDutyCycle(ANGLE.LEFT)
    elif direction == 1:
        servo.ChangeDutyCycle(ANGLE.RIGHT)
    else:
        servo.ChangeDutyCycle(ANGLE.NEUTRAL)
    
def changeSpeed(speed):
    bright.ChangeDutyCycle(speed * 25)

def serverInit():
    '''server initianizing'''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST_, PORT_))
    s.listen(1)
    return s

if __name__ == "__main__":
    main()