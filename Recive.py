import RPi.GPIO as GPIO     # Importing RPi library to use the GPIO pins
import time

Pout = 2
Pin = 3
Freq = .000056
Time = Freq * 4


GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)
GPIO.setup(Pout, GPIO.OUT)     # Declaring GPIO 21 as output pin
GPIO.setup(Pin, GPIO.IN)
#if ( GPIO.input(16) == True ):


def Transmit(x):
	GPIO.output(Pout,GPIO.HIGH) 
	time.sleep(Time)
	GPIO.output(Pout,GPIO.HIGH) 
	time.sleep(Time)
	
	
	for i in range(10):
		if(((x >> i) & 0x0001) == 0x0001):
			GPIO.output(Pout,GPIO.HIGH) 
		else:
			GPIO.output(Pout,GPIO.LOW) 
		time.sleep(Time)

	GPIO.output(Pout,GPIO.HIGH) 
	time.sleep(Time)
	GPIO.output(Pout,GPIO.LOW) 

def TestRecive():
	return (GPIO.input(Pin) == True)

def Recive():
	time.sleep(Freq)
	time.sleep(Time)

	if(!TestRecive()):
		return

	x = 0x0000


	for i in range(10):

		time.sleep(Time)

		if(TestRecive()):
			#tes
			x = (0x0001 << i) | x

	time.sleep(Time)

	if(TestRecive()):
		return x

	return



		

def run():
	

	#Transmit(0x35)
	#n = "aAB"
	
	
	#Transmit(ord(n[0]))
	
	Transmit(0x0001)
	while(1):
		print(Recive())
	
	



try:
	while 1:
		run()
		

		
        

# If Keyborad Interrupt (CTRL+C) is pressed
except KeyboardInterrupt:
	#tes
	#print(input("Test:\n"))
	print("end")
	pass   # Go to next line
