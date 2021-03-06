#from Include import *
import RPi.GPIO as GPIO
import time
import serial
Pout = 16
Freq = .000056
Time = Freq * 4

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)
GPIO.setup(Pout, GPIO.OUT)
#GPIO.setup(Pout, GPIO.IN)
               
ser = serial.Serial(            
     port='/dev/ttyAMA0',
     baudrate = 9600,
     #parity=serial.PARITY_NONE,
     #stopbits=serial.STOPBITS_ONE,
     #bytesize=serial.EIGHTBITS,
     timeout=1
 )
     
     

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
    
while 1:
	ser.write(0x01)
	#Transmit(0x0103)	
	x = 0
	
	#x = ser.read(1)	# Read 1 char
	#x = ser.readline()  

	#print(x)
	'''
	if(x != b''):
		print(x)
	'''
	time.sleep(1)
	#print("hey")
