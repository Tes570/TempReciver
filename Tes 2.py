import smbus
import RPi.GPIO as GPIO

#import firebase
#from firebase import db
from firebase import firebase as Fire


#fireLink = firebase.FirebaseApplication('https://ee175b21.firebaseio.com/')
fireLink = Fire.FirebaseApplication('https://ee175b21.firebaseio.com/')

#firebase.auth()
#db = firebase.database()

#fireLink.put('Demo/Room Setting', 'room0', 14)

t = 0
while(t < 3):
	#result = fireLink.get("Demo/Room Setting/room0", None)
	t = 3
    
	for i in range(0,3):
		#fireLink.put('Demo/Room Setting', ('room' + str(i)), 65)
		fireLink.put('Demo/Room Temp', ('room' + str(i)), 60)
		fireLink.put('Demo/Room Flag', ('room' + str(i)), 0)
    
    #fireLink.put('EE175b21/user/pi', 'cTemp', str(14))
    #print(result)
   
   
   
   
#fireLink.put('EE175b21/user/pi', 'cTemp', str(14))
#fireLink.put('EE175b21/user/pi', 'Hight', str(10))

#result = fireLink.get('EE175b21/user/pi/Hight', None)
#result = ref.child('EE175b21/user/pi').get()

#print(result)
