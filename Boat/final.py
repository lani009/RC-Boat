from socket import *
import RPi.GPIO as GPIO
import time

serverSock = socket(AF_INET,SOCK_STREAM)
serverSock.bind(('',8080))
serverSock.listen(1)


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)


servol = GPIO.PWM(11,50)
bright = GPIO.PWM(7,100)
servol.start(0)
#angle of servol
langle = 9.35  #-29.7
rangle=   5.65#0
cangle = 7.5 #29.7

#bright of led
first = 100
second = 75
third = 50
fourth = 25


def cntm(angle):
    servol.ChangeDutyCycle(angle)
    time.sleep(0.5)
    
def brightchange(number):
    bright.ChangeDutyCycle(number)
    time.sleep(0.5)
    
while True:
    connectionSock, addr = serverSock.accept()
    data = connectionSock.recv(1024)

    print('Get data:',data.decode('utf-8')) 
    connectionSock.send('connecting'.encode('utf-8'))

    if data.decode('utf-8')=='a':
        cntm(langle)
    elif data.decode('utf-8')=='d':
        cntm(rangle)
    elif data.decode('utf-8')=='s':
        cntm(cangle)  
    elif data.decode('utf-8')=='one':
        brightchange(first)
    elif data.decode('utf-8')=='two':
        brightchange(second)
    elif data.decode('utf-8')=='three':
        brightchange(third)
    elif data.decode('utf-8')=='four':
        brightchange(fourth)    
    elif data.decode('utf-8')=='off':
        GPIO.output(7,False)
        
    
    if data.decode('utf-8')=='quit':
        connectionSock.send('quit'.encode('utf-8'))
        break
   
GPIO.cleanup()
