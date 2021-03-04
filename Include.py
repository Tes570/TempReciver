import RPi.GPIO as GPIO     # Importing RPi library to use the GPIO pins
import time
from firebase import firebase as Fire


fireLink = Fire.FirebaseApplication('https://ee175b21.firebaseio.com//')

Pout = 16
ReadStartOut = 17
LedPin = 19
Freq = .000056
Time = Freq * 4


GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)



GPIO.setup(12, GPIO.OUT) 
GPIO.setup(13, GPIO.OUT) 
GPIO.setup(14, GPIO.OUT) 

RoomSet = [0, 0, 0]
RoomTemp = [0, 0, 0]
Servo = [GPIO.PWM(12, 50), GPIO.PWM(13, 50), GPIO.PWM(14, 50)]
Servo[0].start(7.5)
Servo[1].start(7.5)
Servo[2].start(4.5)


for i in range(2, 12):
	GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	#GPIO.setup(i, GPIO.IN), pull_up_down=GPIO.PUD_DOWN

GPIO.setup(Pout, GPIO.OUT)
GPIO.setup(ReadStartOut, GPIO.OUT) 
GPIO.setup(LedPin, GPIO.OUT)

def Setup():
	
	
	
	
	
	for i in range(3):
		RoomSet[i] = fireLink.get(("Demo/Room Setting/room" + str(i)), None)
		RoomTemp[i] = fireLink.get(("Demo/Room Temp/room" + str(i)), None)
		
	#Not using RoomFlag right now.
	
	
	
def ServoOn(x):
	Servo[x].start(2.5)

def ServoOff(x):
	Servo[x].start(7.5)

def FanOn():
	GPIO.output(LedPin,GPIO.LOW) 
	
def FanOff():
	GPIO.output(LedPin,GPIO.HIGH) 
	
def ThermoUpdate():
	
	send = [0x0102, 0x0103]
	###############################################################################
	for i in range(2):
		
		tes = 70
		tes2 = True
		while (tes2):
			Transmit(send[i])
			tem = Recive()
			time.sleep(.001)
			#print(tem)
			#####################
			tes2 = False
			#############################
			
			if((tem >= 55) and (tem <= 100)):
				tes = tem
				tes2 = False
		
		
			
		
		#if(tes2 == False):
			#RoomTemp[i] = tes
		time.sleep(1)
	
def FireUpdate():
	tes = False
	
	for i in range(3):
		RoomSet[i] = fireLink.get(("Demo/Room Setting/room" + str(i)), None)
		RoomTemp[i] = fireLink.get(("Demo/Room Temp/room" + str(i)), None)
		#fireLink.put('Demo/Room Temp', ('room' + str(i)), RoomTemp[i])
		
		if(RoomSet[i] > RoomTemp[i]):
			tes = True
			
	if tes:
		FanOn()
	else:
		FanOff()
		

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
	time.sleep(Time * 80)
	x = 0x0000
	
	for i in range(2, 12):
		if(GPIO.input(i)):
			x = ((0x0001 << (i-2)) | x)
		
	return x
