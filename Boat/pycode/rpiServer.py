import socket
import time
import RPi.GPIO as GPIO

#define global variables -> constant
HOST_ = ""
PORT_ = 1346

#GPIO Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)

servo = GPIO.PWM(11,50)
bright = GPIO.PWM(7,100)
servo.start(0)
bright.start(0)
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
            raw_data = conn.recv(1)
            if not raw_data:
                raise Exception("Client Server Closed")
            speed, direction = parseData(int.from_bytes(raw_data, byteorder='big', signed=False))
            changeRudderAngle(direction)
            changeSpeed(speed)
    except Exception as e:
        print(e)
    finally:
        s.close()
        conn.close()
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
    while True:
        main()