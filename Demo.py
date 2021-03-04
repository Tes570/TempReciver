from Include import *
#import RPi.GPIO as GPIO     # Importing RPi library to use the GPIO pins


def Run():
	
	time.sleep(10)
	
	ThermoUpdate()
	
	FireUpdate()
	print("Hello")
	
	if (RoomSet[0] > RoomTemp[0]):
		ServoOn(0)
		#FanOn
	else:
		ServoOff(0)
	




try:
	#SetUp()
	Setup()
	while 1:
		#t1 = threading.Thread( target=send, args=(0x0103), daemon=True )
		#t1.start()
		#print("het")
		#t1.join()
		Run()
		

		
        

# If Keyborad Interrupt (CTRL+C) is pressed
except KeyboardInterrupt:
	#tes
	#print(input("Test:\n"))
	#GPIO.output(Pout,GPIO.LOW) 
	pass   # Go to next line
