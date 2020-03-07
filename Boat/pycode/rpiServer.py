import socket
import threading
import time

import RPi.GPIO as GPIO
import spidev


class ANGLE():
    '''ANGLE CONSTANT'''
    LEFT = 9.35     #-29.7 degree
    RIGHT = 5.65    #0 degree
    NEUTRAL = 7.5   #29.7 degree

class PIN():
    '''GPIO PINS'''
    BUZZER = 26
    SERVO = 11
    #MOTOR = 7
    Pinout1 = 32
    Pinout2 = 36
    PinENA = 40

#define global variables -> constant
HOST_ = ""
PORT_ = 1346
isBuzz = False

#GPIO Setup
GPIO.setmode(GPIO.BOARD)
#GPIO.setup(PIN.MOTOR, GPIO.OUT)
GPIO.setup(PIN.SERVO, GPIO.OUT)
GPIO.setup(PIN.BUZZER, GPIO.OUT)
GPIO.setup(PIN.MDRIVER, GPIO.OUT)
GPIO.setup(PIN.Pinout1,GPIO.OUT)
GPIO.setup(PIN.Pinout2,GPIO.OUT)
GPIO.setup(PIN.PinENA,GPIO.OUT)

servo = GPIO.PWM(PIN.SERVO, 50)
#speed = GPIO.PWM(PIN.MOTOR, 100)
speed = GPIO.PWM(PIN.PinENA,50)
servo.start(0)
speed.start(0)

#SPI Setup
spi = spidev.SpiDev()
spi.open(0,0)

def main():
    try:
        #socket binding
        s = serverInit()

        #turn the buzzer on
        wifiBuzz(True)
        conn, addr = s.accept()

        #turn the buzzre off
        wifiBuzz(False)
        print("Connection accepted!")
        while True:
            raw_data = conn.recv(4)
            if not raw_data:
                #if data not recived -> connection closing
                raise Exception("Client Server Closed")

            speed, direction = parseData(int.from_bytes(raw_data, byteorder='big', signed=False))
            changeRudderAngle(direction)
            changeSpeed(speed)
            voltage = bytearray()
            voltage.append(getVoltage())
            conn.sendall(voltage)
    except Exception as e:
        print(e)
    finally:
        s.close()
        conn.close()
        GPIO.cleanup()
        print("Connection Closed!")
        
def parseData(data):
    '''parsing data into speed and direction'''
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
    if(speed == 5):
        setReverse()
        speed.ChangeDutyCycle(25)
    else:
        setFoward()
        speed.ChangeDutyCycle(speed * 25)
    
def setFoward():
    GPIO.output(PIN.Pinout1, GPIO.LOW)
    GPIO.output(PIN.Pinout2, GPIO.HIGH)

def setReverse():
    GPIO.output(PIN.Pinout1, GPIO.HIGH)
    GPIO.output(PIN.Pinout2, GPIO.LOW)

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

def getVoltage():
    r = spi.xfer2([1, (8) << 4, 0])
    adc_out = ((r[1]&3) << 8) + r[2]
    return adc_out

def serverInit():
    '''server initianizing'''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST_, PORT_))
    s.listen(1)
    return s

if __name__ == "__main__":
    while True:
        main()
