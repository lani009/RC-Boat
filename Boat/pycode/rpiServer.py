import socket
import threading
import time

import RPi.GPIO as GPIO

class ANGLE():
    '''ANGLE CONSTANT'''
    LEFT = 9.35     #-29.7 degree
    RIGHT = 5.65    #0 degree
    NEUTRAL = 7.5   #29.7 degree

class PIN():
    '''GPIO PINS'''
    BUZZER = 26
    SERVO = 11
    MOTOR = 7

#define global variables -> constant
HOST_ = ""
PORT_ = 1346
isBuzz = False

#GPIO Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN.MOTOR, GPIO.OUT)
GPIO.setup(PIN.SERVO, GPIO.OUT)
GPIO.setup(PIN.BUZZER, GPIO.OUT)

servo = GPIO.PWM(PIN.SERVO, 50)
speed = GPIO.PWM(PIN.MOTOR, 100)
servo.start(0)
speed.start(0)

def main():
    try:
        s = serverInit()
        wifiBuzz(True)
        conn, addr = s.accept()
        wifiBuzz(False)
        print("Connection accepted")
        while True:
            raw_data = conn.recv(1)
            if not raw_data:
                #data not recived -> connection closed
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
    speed.ChangeDutyCycle(speed * 25)

def wifiBuzz(boolean):
    '''Starts the buzzer if the soket connection is still not accepted'''
    global isBuzz
    isBuzz = boolean
    if isBuzz:
        threading.Thread(target=buzzing, daemon=True)
    else:
        for i in range(3):
            GPIO.output(PIN.BUZZER, True)
            time.sleep(0.3)
            GPIO.output(PIN.BUZZER, False)
            time.sleep(0.3)
            GPIO.output(PIN.BUZZER, True)
            time.sleep(0.3)
            GPIO.output(PIN.BUZZER, False)
            time.sleep(0.7)

def buzzing():
    while isBuzz:
        GPIO.output(PIN.BUZZER, True)
        time.sleep(0.5)
        GPIO.output(PIN.BUZZER, False)
        time.sleep(5)

def serverInit():
    '''server initianizing'''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST_, PORT_))
    s.listen(1)
    return s

if __name__ == "__main__":
    while True:
        main()
