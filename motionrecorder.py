import RPi.GPIO as GPIO
import time
import os
from time import sleep
from datetime import datetime

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from one PIR motion sensor, for more than one sensor more input pins need to be added
GPIO.setup(3, GPIO.OUT)         #LED output pin
file = open("/home/pi/Documents/Python/data_log.txt", "a") #workspace path on pi
if os.stat("/home/pi/Documents/Python/data_log.txt").st_size == 0:
        file.write("Time,Sensor1,Sensor2,Sensor3,Sensor4,Sensor5\n")
j=0
while True:
       j=j+1
       i=GPIO.input(11)
       now=datetime.now()
       if i==0:                 #When output from motion sensor is LOW
             file.write(str(now)+","+str(i)+","+"NAN"+","+"NAN"+","+"NAN"+","+"NAN"+"\n") #The NAN's can be replaced by other sensors output
             print "No motion detected",i
             GPIO.output(3, 0)  #Turn OFF LED
             #time.sleep(10)
             file.flush()
             time.sleep(1)#<br/>file.close

       elif i==1:               #When output from motion sensor is HIGH
             file.write(str(now)+","+str(i)+","+"NAN"+","+"NAN"+","+"NAN"+","+"NAN"+"\n") #The NAN's can be replaced by other sensors output
             print "Motion detected",i
             GPIO.output(3, 1)  #Turn ON LED
             #time.sleep(10)
             file.flush()
             time.sleep(1)#<br/>file.close
        
