import RPi.GPIO as GPIO     # Importing RPi library to use the GPIO pins
import time

Pin = 20
Time = .000056 * 4


GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)
GPIO.setup(Pin, GPIO.OUT)     # Declaring GPIO 21 as output pin


def process(x):
	GPIO.output(Pin,GPIO.HIGH) 
	time.sleep(Time)
	GPIO.output(Pin,GPIO.HIGH) 
	time.sleep(Time)
	
	
	for i in range(8):
		if(((x >> i) & 0x01) == 0x01):
			GPIO.output(Pin,GPIO.HIGH) 
		else:
			GPIO.output(Pin,GPIO.LOW) 
		time.sleep(Time)

	GPIO.output(Pin,GPIO.HIGH) 
	time.sleep(Time)
	GPIO.output(Pin,GPIO.LOW) 
		

def run():
	

	#process(0x35)
	#n = "aAB"
	
	
	#process(ord(n[0]))
	
	process(0x65)
	time.sleep(.000056 * 100)
	
	



try:
	while 1:
		run()
		

		
        

# If Keyborad Interrupt (CTRL+C) is pressed
except KeyboardInterrupt:
	#tes
	#print(input("Test:\n"))
	print("end")
	pass   # Go to next line
