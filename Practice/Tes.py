import smbus
import RPi.GPIO as GPIO

from firebase import firebase as Fire


fireLink = Fire.FirebaseApplication('https://ee175b21.firebaseio.com/')



while(1):
    result = fireLink.get("Demo/Room Setting/room0", None)
    print(result)
    print(type(result))
   
   
   
   
#fireLink.put('EE175b21/user/pi', 'cTemp', str(14))
