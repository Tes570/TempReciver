from Include import *
#import RPi.GPIO as GPIO     # Importing RPi library to use the GPIO pins


def Run():
	
	time.sleep(1)
	ServoTest()
	time.sleep(2)
	ServoReset()
	time.sleep(5)




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
