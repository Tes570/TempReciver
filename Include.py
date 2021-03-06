import RPi.GPIO as GPIO     # Importing RPi library to use the GPIO pins
import time
from firebase import firebase as Fire


fireLink = Fire.FirebaseApplication('https://ee175b21.firebaseio.com//')

Pout = 16
Con = 10
Cout = 11
LedPin = 19
Freq = .000056
Time = Freq * 4

ServoTest = False


GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)



GPIO.setup(12, GPIO.OUT) 
GPIO.setup(13, GPIO.OUT) 
GPIO.setup(14, GPIO.OUT) 

RoomSet = [0, 0, 0]
RoomTemp = [0, 0, 0]
Servo = [GPIO.PWM(12, 50), GPIO.PWM(13, 50), GPIO.PWM(14, 50)]
Servo[0].start(2.5)
Servo[1].start(2.5)
Servo[2].start(2.5)


for i in range(2, 10):
	GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	#GPIO.setup(i, GPIO.IN), pull_up_down=GPIO.PUD_DOWN

GPIO.setup(Pout, GPIO.OUT)
GPIO.setup(Con, GPIO.OUT)
GPIO.setup(Cout, GPIO.OUT)
GPIO.setup(LedPin, GPIO.OUT)



def Setup():
	
	
	GPIO.output(Con,GPIO.LOW)
	
	
	for i in range(3):
		RoomSet[i] = fireLink.get(("Demo/Room Setting/room" + str(i)), None)
		RoomTemp[i] = fireLink.get(("Demo/Room Temp/room" + str(i)), None)
		
	#Not using RoomFlag right now.
	
	
	
def ServoOn(x):
	Servo[x].start(7.5)

def ServoOff(x):
	Servo[x].start(2.5)

def FanOn():
	GPIO.output(LedPin,GPIO.LOW) 
	
def FanOff():
	GPIO.output(LedPin,GPIO.HIGH) 
	
def ThermoUpdate():
	
	send = [0x0101, 0x0102]
	###############################################################################
	for i in send:
		print("room: " + str(i))
		RoomTemp[send.index(i)] = Thermo(i)
		
	
def FireUpdate():
	ServoTest = False
	
	for i in range(3):
		RoomSet[i] = fireLink.get(("Demo/Room Setting/room" + str(i)), None)
		#RoomTemp[i] = fireLink.get(("Demo/Room Temp/room" + str(i)), None)
		fireLink.put('Demo/Room Temp', ('room' + str(i)), RoomTemp[i])
		
		if(RoomSet[i] > RoomTemp[i]):
			ServoTest = True
			
	if ServoTest:
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


def Thermo(xn):
	
	#Transmit(0x0203)
	#time.sleep(.01)
	#tes = Recive()
	GPIO.output(Con,GPIO.HIGH)
	
	
	tes = 0
	tem = 3
	while((tes == 0) and (tem != 0)):
		Transmit(xn)
		
		time.sleep(.5)
		tes = Recive()
		tem = tem - 1
		
		if((tes != 0) and (tes != 0xff)):
			#tes = Recive()
			#print(hex(tes))
			print(tes)
			if((tes > 110) or (tes < 40)):
				tes = 0
		else:
			tes = 0
			
					
	
	
	
	
	time.sleep(10)
	GPIO.output(Con,GPIO.LOW)
	time.sleep(.01)
	
def ServoOpen():


	if(RoomSet[0] < RoomTemp[0]):
		ServoOn(0)

	if(RoomSet[1] < RoomTemp[1]):
		ServoOn(1)
		ServoOn(2)



def ServoClose():
	if(RoomSet[0] > RoomTemp[0]):
		ServoOff(0)

	if(RoomSet[1] > RoomTemp[1]):
		ServoOff(1)
		ServoOff(2)


