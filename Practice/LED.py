import RPi.GPIO as GPIO     # Importing RPi library to use the GPIO pins




GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)


Pout = 19


GPIO.setup(Pout, GPIO.OUT)
GPIO.output(Pout,GPIO.HIGH) 




try:
	#SetUp()
	while 1:
		#t1 = threading.Thread( target=send, args=(0x0103), daemon=True )
		#t1.start()
		print("het")
		#t1.join()
		

		
        

# If Keyborad Interrupt (CTRL+C) is pressed
except KeyboardInterrupt:
	#tes
	#print(input("Test:\n"))
	GPIO.output(Pout,GPIO.LOW) 
	pass   # Go to next line
