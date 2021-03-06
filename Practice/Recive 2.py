import RPi.GPIO as GPIO     # Importing RPi library to use the GPIO pins
import time
import threading

Pout = 16
Test = 3


Freq = .000056
#Freq = .001
Time = Freq * 4





GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

GPIO.setup(Pout, GPIO.OUT)
#GPIO.setup(Test, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Test, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#PUD_DOWN
#GPIO.add_event_detect(Test, GPIO.RISING)



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
	#Test
	
	x = 0x0000
	#while(not GPIO.event_detected(Test)):
	while(not GPIO.input(Test)):
		time.sleep(Freq)
	
	
	#time.sleep(Freq)
	#print("hey")
	if(GPIO.input(Test)):
		for i in range(10):
			time.sleep(Time)
			x = ((0x0001 << (i)) | x)
				
		
		
	
	
		
	return x



		

def run():
	Transmit(0x0103)
	#tes = Recive()
	tes = 0
	time.sleep(Time * 100)
	print(GPIO.input(Test))
	
	
	
	


 

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
