import RPi.GPIO as GPIO     # Importing RPi library to use the GPIO pins
import time

Pin = 20
Time = .000056 * 4


GPIO.setmode(GPIO.BCM) 
GPIO.setup(Pin, GPIO.OUT)     # Declaring GPIO 21 as output pin



try:
	while 1:
		
		GPIO.output(Pin,GPIO.HIGH) 

		time.sleep(Time)

		GPIO.output(Pin,GPIO.LOW) 
		time.sleep(Time)

		
        

# If Keyborad Interrupt (CTRL+C) is pressed
except KeyboardInterrupt:
	#tes
	print("end")
	pass   # Go to next line