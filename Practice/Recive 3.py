import RPi.GPIO as GPIO     # Importing RPi library to use the GPIO pins
import time
import threading

Pout = 16
Con = 10
Cout = 11


Freq = .000056
#Freq = .001
Time = Freq * 4





GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

GPIO.setup(Pout, GPIO.OUT)
GPIO.setup(Con, GPIO.OUT)
GPIO.setup(Cout, GPIO.OUT)
#GPIO.setup(Test, GPIO.IN, pull_up_down=GPIO.PUD_UP)

for i in range(2, 10):
	GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	#GPIO.setup(i, GPIO.IN)
	
GPIO.output(Con,GPIO.LOW)
#GPIO.setup(Cout, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#PUD_DOWN


def Transmit(x):
	GPIO.output(Cout,GPIO.HIGH)
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
	GPIO.output(Cout,GPIO.LOW)


def Recive():
	#time.sleep(Freq)
	#Test
	
	x = 0x0000
	
	
	
	#time.sleep(Freq)
	for i in range(2, 10):
		if(GPIO.input(i)):
			x = ((0x0001 << (i-2)) | x)
				
		
		
	
	
		
	return x

def send():
	x = 0x0103
	while(1):
		Transmit(x)
		time.sleep(1)

		

def Thermo(xn):
	
	#Transmit(0x0203)
	#time.sleep(.01)
	#tes = Recive()
	GPIO.output(Con,GPIO.HIGH)
	
	t = 0
	
	#while(t < 1):
	t = t + 1
	#GPIO.output(Con,GPIO.LOW)
	Transmit(xn)
	#GPIO.output(Con,GPIO.HIGH)
	n = 0
	#while (n < 2):
			
	n = n + 1
	tes = 0
	time.sleep(.5)
	tes = Recive()
	
		
	#time.sleep(Freq)
	if((tes != 0)and (tes != 0xff)):
		#tes = Recive()
		print(hex(tes))
		print(tes)
		n = 100000
		t = 10000
				
	#GPIO.output(Con,GPIO.LOW)
	
	
	
	time.sleep(10)
	GPIO.output(Con,GPIO.LOW)
	time.sleep(.01)
	


 

try:
	#SetUp()
	#t1 = threading.Thread( target=send, daemon=True )
	#t1.start()
	
	while 1:
		print("Room 1")
		Thermo(0x0101)
		
		print("Room 2")
		Thermo(0x0102)	
		#t1.join()
		

		
        

# If Keyborad Interrupt (CTRL+C) is pressed
except KeyboardInterrupt:
	#tes
	#print(input("Test:\n"))
	print("end")
	pass   # Go to next line
