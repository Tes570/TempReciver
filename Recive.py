import RPi.GPIO as GPIO     # Importing RPi library to use the GPIO pins
import time
import threading

Pout = 2
Pin = 3
#Freq = .000056
Freq = .001
Time = Freq * 4


GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)
GPIO.setup(Pout, GPIO.OUT)     # Declaring GPIO 21 as output pin
GPIO.setup(Pin, GPIO.IN)
#if ( GPIO.input(16) == True ):

def send(x):
	Transmit(x)
	i = 0
	while(i < 5000):
		i = i + 1
		time.sleep(Freq)

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

def TestRecive(): #is it groud?
	return (GPIO.input(Pin))

def Recive():
	#time.sleep(Freq)
	GPIO.output(Pout,GPIO.HIGH)
	time.sleep(Time)
	GPIO.output(Pout,GPIO.LOW)

	if(TestRecive() == False):
		return 0

	x = 0x0000
	
	 

	for i in range(10):

		time.sleep(Time)
		GPIO.output(Pout,GPIO.HIGH)
		time.sleep(Freq)
		if(TestRecive()):
			#tes
			x = (0x0001 << i) | x
			
		GPIO.output(Pout,GPIO.LOW) 
		#print(hex(x))

	GPIO.output(Pout,GPIO.HIGH)
	time.sleep(Time)
	GPIO.output(Pout,GPIO.LOW) 

	if(TestRecive()):
		return x

	return 0



		

def run():
	

	#Transmit(0x35)
	#n = "aAB"
	
	
	#Transmit(ord(n[0]))
	
	#Transmit(0x0103)
	i = 0
	while(i < 5000):
		#i = i + 1
		time.sleep(Freq)
		
		if(TestRecive()):
			#print("HELP")
			nit = Recive()
			if(nit != 0):
				print(hex(nit))
			
	
	




try:
	while 1:
		#t1 = threading.Thread( target=send, args=(0x0103), daemon=True )
		#t1.start()
		run()
		#t1.join()
		

		
        

# If Keyborad Interrupt (CTRL+C) is pressed
except KeyboardInterrupt:
	#tes
	#print(input("Test:\n"))
	print("end")
	pass   # Go to next line
