#Import the GPIO on the pi to access the pins and import time to use the sleep functions
import RPi.GPIO as GPIO
import time

#Set the board as a bcm to use the pins warnings and warnings can be false because they are unnecessary 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Define the pins  
Control = 27
Red = 20
Green = 18
Blue = 17

#setup all of the pins 
GPIO.setup(Red, GPIO.OUT) 
GPIO.setup (Green, GPIO.OUT)
GPIO.setup(Blue, GPIO.OUT)

GPIO.setup(Control, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.output(Green, GPIO.LOW)
GPIO.output(Red, GPIO.LOW)
GPIO.output(Blue, GPIO.LOW)

def stoplight():
	print ('Green LED on')
	GPIO.output(Green, GPIO.HIGH)
	GPIO.output(Red, GPIO.LOW)
	time.sleep(5)
	print ('Green LED off')
	GPIO.output(Green, GPIO.LOW)
	print ('Yellow LED on')
	GPIO.output(Green, GPIO.HIGH)
	GPIO.output(Red, GPIO.HIGH)
	time.sleep(1)
	print ('Yellow LED off')
	GPIO.output(Green, GPIO.LOW)
	GPIO.output(Red, GPIO.LOW)
	print ('Red LED on')
	GPIO.output(Red, GPIO.HIGH)
	time.sleep(4)
	print ('Red LED off')
	GPIO.output(Red, GPIO.LOW)	
		
while True:
	if GPIO.input(Control) == GPIO.LOW:
		stoplight()

#GPIO.cleanup






