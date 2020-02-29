from socket import *

serverSock = socket(AF_INET,SOCK_STREAM)
serverSock.bind(('',8080))
serverSock.listen(1)

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)



while True:
    connectionSock, addr = serverSock.accept()
    data = connectionSock.recv(1024)

    print('Get data:',data.decode('utf-8'))
    if data.decode('utf-8') == 'go':
        servol = GPIO.PWM(11,50) # 11 is pin, 50 == 50hz pulsive

        servol.start(0)
        print("Wait 2 sec")
        time.sleep(2)

        #define variable duty

        duty = 2

        while duty <=6:
            servol.ChangeDutyCycle(duty)
            time.sleep(1)
            duty = duty+1

        time.sleep(2)

        
        servol.ChangeDutyCycle(2)
        time.sleep(0.5)
        servol.ChangeDutyCycle(0)
        
        servol.stop()
        GPIO.cleanup()    

    connectionSock.send('server.'.encode('utf-8'))
    if data.decode('utf-8')=='quit':
        connectionSock.send('quit'.encode('utf-8'))
    
    print('send message')

    if data.decode('utf-8')=='quit':
        break
