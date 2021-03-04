

import RPi.GPIO as GPIO
import time
import serial
Pout = 15
Freq = .000056
Time = Freq * 4

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)
#GPIO.setup(Pout, GPIO.OUT)
GPIO.setup(Pout, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


F_CPU = 1000000
#define F_CPU 64000UL 
BAUD_RATE = 50
BAUD_PRESCALE = (((F_CPU / (BAUD_RATE * 16))) - 1)
               
ser = serial.Serial(            
     port='/dev/ttyAMA0',
     #baudrate = 9600,
     baudrate = BAUD_PRESCALE,
     #parity=serial.PARITY_NONE,
     #stopbits=serial.STOPBITS_ONE,
     #bytesize=serial.EIGHTBITS,
     timeout=1
)

counter = 0

while 1:
	
	x = 0
	
	#x = ser.read(1)	# Read 1 char
	#x = ser.readline() 
	#print(x)
	
	
	#ser.write('Write counter: %d \n'%(counter))
	ser.write(0x02)
	time.sleep(1)
	#counter += 1




