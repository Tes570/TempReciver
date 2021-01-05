import RPi.GPIO as GPIO     # Importing RPi library to use the GPIO pins
import smbus

from firebase import firebase as Fire



GPIO.setmode(GPIO.BCM) 



class FireData:

	def __init__(self):
		self.fireLink = Fire.FirebaseApplication('https://ee175b21.firebaseio.com/')

	def get(self, room, value):
		return self.fireLink.get(("Demo//Room Setting//room" + str(room) + "//" + str(value)), None)




class PinCon:

	def __init__(self, pin):
		self.pin = pin
		GPIO.setup(self.pin, GPIO.OUT)     # Declaring GPIO 21 as output pin
		self.p = GPIO.PWM(self.pin, 50)     # Created PWM channel at 50Hz frequency
		self.p.start(2.5)
		self.ON = False

	def set(self, deg):
		T = (10/180)*deg + 2.5
		self.p = self.p.ChangeDutyCycle(T)

		if deg != 0:
			self.ON = False
		else:
			self.ON = True

	def get(self):
		return self.ON


Pins = [PinCon(16), PinCon(20), PinCon(21)]



try:
    while 1:                    # Loop will run forever

    	print(Pins[0].get())
    	

# If Keyborad Interrupt (CTRL+C) is pressed
except KeyboardInterrupt:
    pass   # Go to next line


GPIO.cleanup()  