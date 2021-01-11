import RPi.GPIO as GPIO     # Importing RPi library to use the GPIO pins
import smbus

from firebase import firebase as Fire


fireLink = Fire.FirebaseApplication('https://ee175b21.firebaseio.com//')

GPIO.setmode(GPIO.BCM) 



class FireData:


    def __init__(self, tem):
	#demo
        self.Rooms = tem
        self.On = False
        

    def get_setting(self, room):
        return fireLink.get(("Demo//Room Setting//room" + str(room)), None)

    def get_temp(self, room):
        return fireLink.get(("Demo//Room Temp//room" + str(room)), None)


class FireCon:



    def __init__(self, tem):
	#demo
        self.Pins = tem
        self.setting = [[0, 0, 0, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
        self.turn = [False, False, False]
        self.cur = [0, 0, 0, 0]

        self.open = 0
        self.close = 90

    def update(self, tem, bo):
    	self.turn[tem] = bo

    def run(self):

    	self.cur = [0, 0, 0, 0]

    	for i in len(self.cur):
    		for t in len(self.setting):
    			if(self.setting[t][i] == 1):
    				self.cur[i] = 1
        



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


Pins = [PinCon(16), PinCon(20), PinCon(21), PinCon(12)]

Con = FireCon(Pins)

OData = FireData(3)

try:
	while 1:

		for i in range(OData.Rooms):
			if(OData.get_temp(i) > OData.get_setting(i)):
				Con.update(i, True)
			else:
				Con.update(i, False)
		Con.run()
		print(Con.cur)

        

# If Keyborad Interrupt (CTRL+C) is pressed
except KeyboardInterrupt:
    #tes
    print("end")
    pass   # Go to next line


GPIO.cleanup()  