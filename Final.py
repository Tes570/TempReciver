import RPi.GPIO as GPIO     # Importing RPi library to use the GPIO pins
import smbus


from firebase import firebase as Fire



GPIO.setmode(GPIO.BCM) 
fireLink = Fire.FirebaseApplication('https://ee175b21.firebaseio.com/')

class PinCon:

	def __init__(self, pin):
		self.pin = pin
		GPIO.setup(self.pin, GPIO.OUT)     # Declaring GPIO 21 as output pin
		self.p = GPIO.PWM(self.pin, 50)     # Created PWM channel at 50Hz frequency
		self.p.start(2.5)

	def set(self, deg):
		self.p = self.p.ChangeDutyCycle(2.5)




try:
    while 1:                    # Loop will run forever

    	result = fireLink.get("Demo/Room Setting/room0", None)
    	print(result)
    	
        p.ChangeDutyCycle(2.5)  # Move servo to 0 degrees
        sleep(1)                # Delay of 1 sec
        p.ChangeDutyCycle(7.5)  # Move servo to 90 degrees
        sleep(1)                
        #p.ChangeDutyCycle(12.5) # Move servo to 180 degrees
        #sleep(1)
# If Keyborad Interrupt (CTRL+C) is pressed
except KeyboardInterrupt:
    pass   # Go to next line


GPIO.cleanup()  