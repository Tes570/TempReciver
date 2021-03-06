import RPi.GPIO as GPIO     # Importing RPi library to use the GPIO pins
import time
import threading

Pout = 16
ReadStartOut = 17
LedPin = 19


Freq = .000056
#Freq = .001
Time = Freq * 4





GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

for i in range(2, 12):
	GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	#GPIO.setup(i, GPIO.IN)

#GPIO.setup(ReadStartIn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(ReadStartIn, GPIO.IN)


GPIO.setup(ReadStartOut, GPIO.OUT)
GPIO.setup(Pout, GPIO.OUT)



#GPIO.output(Pout,GPIO.LOW)
GPIO.output(ReadStartOut,GPIO.LOW)


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


def Recive():
	#time.sleep(Freq)
	x = 0x0000
	
	for i in range(2, 12):
		if(GPIO.input(i)):
			x = ((0x0001 << (i-2)) | x)
		
	return (x & 0x03)



		

def run():
	

	#Transmit(0x35)
	#n = "aAB"
	
	
	#Transmit(ord(n[0]))
	#GPIO.output(ReadStartOut,GPIO.HIGH)
	GPIO.output(ReadStartOut,GPIO.LOW)
	Transmit(0x0102)
	print("Send")
	'''
	i = 0
	time.sleep(Time * 200)
	
	nit = Recive()
			
	if((nit != 0) and (nit != 0x3ff)):
		#i = 101
		time.sleep(Time * 10)
		#print(hex(nit))
		print(nit)
			
	'''
	
	#time.sleep(Time * 10)
	#time.sleep(Freq * 100)
	time.sleep(.01)
	


 

try:
	#SetUp()
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
